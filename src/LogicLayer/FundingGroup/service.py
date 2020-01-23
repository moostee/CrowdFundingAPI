from DataAccessLayer.FundingGroup.serializer import FundingGroupSerializer
from DataAccessLayer.DataModule import DataModule
from Utility.Response import Response
from Utility.Utility import Utility
from Utility.logger import Logger
from Utility.Validator import Validator
import uuid
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
import json
from datetime import date

class FundingGroupService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('Logiclayer.FundingGroupService')
        self.requestId = uuid.uuid4()

    def createFundinGroup(self,data,user):
        try:
            adminRole = self.data.roleRepository.getAdmin()
            if 'fundingGroupType' not in data.keys(): raise ValidationError(json.dumps({"fundingGroupType": ["Funding group type is required."]}))

            validData = FundingGroupSerializer(data=data)
            if not validData.is_valid(): raise ValidationError(json.dumps(validData.errors))
            
            fundingGroupType = self.data.fundingGroupTypeRepository.getOne(data['fundingGroupType'])
            rules = self.__getRequiredFundingGroupRules(fundingGroupType,data)
            validate = Validator(data, rules).validate()

            if not validate.isValid:
                validateError = "failed validation for {} funding group type".format(fundingGroupType.name)
                raise ValidationError(json.dumps(validate.errors))
            
            data,fundingSource,beneficiarySource = self.__cleanUpData(data,fundingGroupType,user)

            if not fundingSource or not beneficiarySource:
                validateError = {"beneficiarySource | FoundSource":["Beneficiary or funding source violation"]}
                raise ValidationError(json.dumps(validateError))

            savedFundingGroup = self.data.fundingGroupRepository.create(data)

            fundingGroupAdminData = self.__getFundingGroupUser(data,savedFundingGroup,fundingSource,beneficiarySource,adminRole)
            self.data.fundingGroupUserRepository.create(fundingGroupAdminData)

            self.logger.Info(r"Funding group with id --> {} was successfully created, n\ REQUESTID => {}".format(data,self.requestId))
            return Response.success(self.requestId, data=FundingGroupSerializer(savedFundingGroup,many=False).data),201
        except ValidationError as ex:
            self.logger.Info(r"Funding group with data \"{}\" could not be validated  with error {} n\ REQUESTID => {}".format(data,json.loads(ex.message),self.requestId))
            return Response.error(self.requestId, message="Error occured validating your request.", error=json.loads(ex.message), responseCode='01'),400
        except IntegrityError as ex:
            self.logger.Info(r"Funding group with details --> {} was not created. Integrity error exception occured: {} already exist. n\ REQUESTID => {}".format(data,str(ex),self.requestId))
            return Response.error(self.requestId, message='Please try again. Something unexpected happend.', error=r"{} funding group already exist".format(data['name']), responseCode='01'),409
        except ObjectDoesNotExist as ex:
            self.logger.Info(r"Funding group with details --> {} was not created. Database setup error occured: {}. n\ REQUESTID => {}".format(data,str(ex),self.requestId))
            return Response.error(self.requestId, message='Funding group cannot be created at this time. Please contact the administrator.', error="Resource not found.", responseCode='03'),404
        except BaseException as ex:
            self.logger.Info(r"Funding group with details: --> {} was not created. An exception occured: {}, n\ REQUESTID => {}".format(data,str(ex),self.requestId))
            return Response.error(self.requestId, error=str(ex)),500

    def getFundingGroups(self,user=None):
        try:
            data = self.data.fundingGroupRepository.getAll()
            self.logger.Info(r"Successfully fetched all Funding group, requestId --> {}".format(self.requestId))
            return Response.success(self.requestId, data=FundingGroupSerializer(data, many=True).data)
        except Exception:
            self.logger.Info(r"Unable to fetch all Funding group due to exception--> {}, requestId --> {}".format(str(Exception), self.requestId))
            return Response.error(self.requestId, error=str(Exception))

    def __getRequiredFundingGroupRules(self,fundingGroupType,data):
        rules = {
            "fundingSource":"uuid",
            "beneficiarySource": "uuid",
            "startDate":"after:{}".format(date.today()),
        }
        if fundingGroupType.hasFixedIndividualAmount or fundingGroupType.hasFixedGroupAmount:
            rules['individualAmount'] = 'number'
            rules['currency'] = 'string'
        
        if fundingGroupType.hasMaturityDate:
            rules['targetGroupDate'] = "after:{}".format(data['startDate'])
        
        if fundingGroupType.hasFixedDefaultCycle or fundingGroupType.hasRollingBeneficiary:
            if not fundingGroupType.defaultCycleDuration or 'cycleDuration' in data:
                rules['cycleDuration'] = "pattern:\\d+(d|w|m)"
        
        return rules
    
    def __getNextCycleDate(self,fundingGroupType,data):
        if fundingGroupType.hasFixedDefaultCycle or fundingGroupType.hasRollingBeneficiary:
            return Utility.computeNextCycleDate(data['cycleDuration'], data['startDate'])
        return data['targetGroupDate']

    def __cleanUpData(self,data,fundingGroupType,user):
        data['fundingGroupType'] = fundingGroupType
        data['nextCycleDate'] = self.__getNextCycleDate(fundingGroupType,data)
        data["code"] = Utility.randomString(7)
        data['initiator'] = self.data.userRepository.getOne(user['id'])
        fundingSource = self.data.fundingSourceRepository.getOne(data.pop('fundingSource', None))
        beneficiarySource =  self.data.beneficiarySourceRepository.getOne(data.pop('beneficiarySource', None))
        data['cycleDuration'] = data['cycleDuration'] or fundingGroupType.cycleDuration
        return data,fundingSource,beneficiarySource
    
    def __getFundingGroupUser(self,data,fundingGroup,fundingSource,beneficiarySource,role):
        props = ['user', 'fundingGroup', 'userSequence', 'initiator']
        data = {("user" if field == 'initiator' else field):value for (field,value) in data.items() if field in props}
        data['beneficiarySource'] = beneficiarySource
        data['fundingSource'] = fundingSource
        data['role'] = role
        data['balance'] = 0.0
        data['status'] = 'Approved'
        data['fundingGroup'] = fundingGroup
        data['userSequence'] = 0
        return data
