from django.db import IntegrityError
from django.utils import timezone
from DataAccessLayer.Funding.model import Funding as FundingModel
from DataAccessLayer.User.model import User
from DataAccessLayer.FundingGroup.model import FundingGroup
from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.Funding.serializer import FundingSerializer
from Utility.Response import Response
from Utility.logger import Logger
from Utility.Utility import Utility

import uuid
class FundingService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.FundingService')

    def createFunding(self, data):
        requestId = uuid.uuid4()

        try:
            validData = FundingSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"Funding with data \"{}\" validation error {} n\ REQUESTID => {}".format(data, validData.errors, requestId))
                return Response.error(requestId, error=validData.errors, responseCode='01'), 400

            boolean, field = self.__doesFieldExist(data)
            if boolean == False:
                self.logger.Info(r"Missing {} field. {} id must be provided n\ REQUESTID => {}".format(field, field, requestId))
                return Response.error(requestId, error={ r"{}".format(field): [ 'This field is required' ]}, responseCode='01'), 400

            if self.data.fundingRepository.doesBeneficiaryExist(data['beneficiary'], data['fundingGroup']):
                self.logger.Info(r"Existing Beneficiary. Beneficiary Already exisits for funding group n\ REQUESTID => {}".format(requestId))
                return Response.error(requestId, message='Beneficiary Already Exists for this funding group', responseCode='01'), 409
            
            beneficiary = self.data.userRepository.getOne(data['beneficiary'])
            fundingGroup = self.data.fundingGroupRepository.getOne(data['fundingGroup'])

            dataToCreate = {
                'beneficiary': beneficiary,
                'fundingGroup': fundingGroup,
                'cycle': data['cycle'],
                'amount': data['amount'],
                'currency': data['currency'],
                'dueDate': data['dueDate']
                }

            savedFunding = self.data.fundingRepository.create(dataToCreate)
            self.logger.Info(r"Funding was successfully created, n\ REQUESTID => {}".format(requestId))
            return Response.success(requestId, data=FundingSerializer(savedFunding, many=False).data), 201

        except IntegrityError:
            self.logger.Info(r"Funding was not created. Funding already exists. n\ REQUESTID => {}".format(requestId))
            return Response.error(requestId, error="Funding already exists", responseCode='01'), 400

        except BaseException as ex:
            self.logger.Info(r"Funding was not created. An exception occured: {}, n\ REQUESTID => {}".format(str(ex),requestId))
            return Response.error(requestId, error=str(ex)), 400

    def getAllFundings(self):
        requestId = uuid.uuid4()

        try:
            data = self.data.fundingRepository.getAll()
            self.logger.Info(r"Successfully fetched all fundings, requestId --> {}".format(requestId))
            return Response.success(requestId, data=FundingSerializer(data, many=True).data), 200

        except BaseException as ex:
            self.logger.Info(r"Unable to fetch all fundings due to exception --> {}, requestId --> {}".format(str(ex), requestId))
            return Response.error(requestId, error=str(ex)), 400

    def __doesFieldExist(self, requestBody):
        if 'beneficiary' not in requestBody:
            return False, 'beneficiary'
        
        elif 'fundingGroup' not in requestBody:
            return False, 'fundingGroup'
        
        else:
            return True, None