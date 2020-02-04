from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.BeneficiarySource.serializer import BeneficiarySourceSerializer,DeleteBeneficiarySourceSerializer,CreateBeneficiarySourceSerializer
from Utility.Response import Response
import uuid
import json
from Utility.logger import Logger

class BeneficiarySourceService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.BeneficiarySourceService')
    
    def getFundingSourcesForUser(self,userId):
        
        try:
            requestId = uuid.uuid4()
            if self.data.beneficiarySourceRepository.HasBeneficiarySource(userId) is False:
                self.logger.Info("User -->{0}does not have a beneficiary source(s), n\ REQUESTID =>{1}".format(userId,requestId))
                return Response.success(requestId,"User does not have any beneficiary source(s)",responseCode="03"),404
            
            userBeneficiarySource = self.data.beneficiarySourceRepository.GetUserBeneficiarySource(userId)
            responseData = BeneficiarySourceSerializer(userBeneficiarySource,many=True).data
            self.logger.Info("Successfully got beneficiary source(s) for user {0},n\ REQUESTID => {1}".format(userId,requestId))

        except Exception as exception :
            self.logger.Error(exception)
            return Response.error(requestId),500
        
        return Response.success(requestId,data=responseData),200

    

    def createBeneficiarySourcesForUser(self,userId,data):
        
        try:
            requestId = uuid.uuid4()
           
            validData = CreateBeneficiarySourceSerializer(data=data)
            if(validData.is_valid() is False): 
                self.logger.Info("Validation error for user {0},n\ REQUESTID => {1}".format(userId,requestId))
                return Response.error(requestId,message="Validation Error",responseCode="01",error=validData.errors),400

            #validate issuer exists
            if not self.data.issuerRepository.IsExists(validData.data['issuerId']):
                self.logger.Info("Issuer Id not found{0},n\ REQUESTID => {1}".format(userId,requestId))
                return Response.error(requestId,message="Issuer does not exist, kindly contact the admin.",responseCode="01"),404

            #validate beneficiarySourceType exists
            if not self.data.beneficiarySourceTypeRepository.IsExists(validData.data['beneficiarySourceTypeId']):
                self.logger.Info("beneficiary source type Id not found{0},n\ REQUESTID => {1}".format(userId,requestId))
                return Response.error(requestId,message="beneficiary source type does not exist, kindly contact the admin.",responseCode="01"),404

            # validate account details
            if(self.data.beneficiarySourceRepository.CheckIfUserDestinationAccountExists(validData.data['issuerId'],validData.data['beneficiarySourceTypeId'],validData.data['destinationNumber'])): 
                self.logger.Info("Account credentials already exists {0},n\ REQUESTID => {1}".format(userId,requestId))
                return Response.error(requestId,message="Account credentials already exists.",responseCode="01"),409            
            
            # Create Beneficiary source
            beneficiarySourceModel = self.MapBeneficiarySourceModel(validData.data,userId)            
            createdUserBeneficiarySource = self.data.beneficiarySourceRepository.create(beneficiarySourceModel)
            self.logger.Info("Successfully created beneficiary source for user {0},n\ REQUESTID => {1}".format(userId,requestId))
            
            # Create beneficiary source property
            properties = validData.data.pop('property')
            beneficiarySourcePropertyModels = self.MapBeneficiarySourcePropertyModel(createdUserBeneficiarySource,properties)
            createdBeneficiarySourceProperty = self.SaveBeneficiarySourceProperty(beneficiarySourcePropertyModels)            

            if createdBeneficiarySourceProperty is None:
                self.logger.Info("beneficiary source property not successfully created for beneficiary source id => {0} for user {1},n\ REQUESTID => {2}".format(createdUserBeneficiarySource.id,userId,requestId))
                self.data.beneficiarySourceRepository.DeleteUserBeneficiarySource(userId,createdUserBeneficiarySource.id)
                return Response.error(requestId,message="Beneficiary source was not successfully created. Please try again later.",responseCode="01"),200 

            responseData = BeneficiarySourceSerializer(createdUserBeneficiarySource,many=False).data
            self.logger.Info("beneficiary source property successfully created for beneficiary source id => {0} for user {1},n\ REQUESTID => {2}".format(createdUserBeneficiarySource.id,userId,requestId))           
            
        except Exception as exception :
            self.logger.Error(exception)
            return Response.error(requestId),500
        
        return Response.success(requestId,data=responseData),201



    def deleteBeneficiarySourcesForUser(self,userId,data):
        
        try:
            requestId = uuid.uuid4()

            validData = DeleteBeneficiarySourceSerializer(data=data)
            if(validData.is_valid() is False): return Response.error(requestId,message="Validation Error",responseCode="01",error=validData.errors),400
            data = validData.data;
            if self.data.beneficiarySourceRepository.IsExists(data['beneficiaryId']) is False:
                self.logger.Info(" -->{0}beneficiary source does not exist, n\ REQUESTID =>{1}".format(userId,requestId))
                return Response.success(requestId,"beneficiary source does not exist",responseCode="03"),404            

            if self.data.beneficiarySourceRepository.HasBeneficiarySource(userId) is False:
                self.logger.Info("User -->{0}does not have a beneficiary source(s), n\ REQUESTID =>{1}".format(userId,requestId))
                return Response.success(requestId,"User does not have any beneficiary source(s)",responseCode="03"),404
            
            if self.data.beneficiarySourceRepository.CheckUserIsTiedToBeneficiarySource(userId,data['beneficiaryId']) is False:
                self.logger.Info("User -->{0}doesn't have this beneficiary source(s), n\ REQUESTID =>{1}".format(userId,requestId))
                return Response.success(requestId,"User does not have this beneficiary source(s)",responseCode="03"),404
            
            deletedUserBeneficiarySource = self.data.beneficiarySourceRepository.DeleteUserBeneficiarySource(userId,data['beneficiaryId'])

            if deletedUserBeneficiarySource <= 0:
                self.logger.Info(r"""REQUESTID => {} n\ Beneficiary source with ID => {} could not be deleted.""".format(requestId,validData['beneficiaryId']))
                return Response.error(requestId,"Delete not successful. Please try again later.",responseCode="03"),200

            self.logger.Info("Successfully created beneficiary source for user {0},n\ REQUESTID => {1}".format(userId,requestId))

        except Exception as exception :
            self.logger.Error(exception)
            return Response.error(requestId),500
        
        return Response.success(requestId,data="Beneficiary source was successfully deleted."),200

    
    def MapBeneficiarySourceModel(self,inputData,userId):
        return {
            "user" : self.data.userRepository.getOne(userId),
            "beneficiarySourceType" : self.data.beneficiarySourceTypeRepository.getOne(inputData['beneficiarySourceTypeId']),
            "destinationNumber" : inputData['destinationNumber'],
            "issuer" : self.data.issuerRepository.getOne(inputData['issuerId'])
        }

    def MapBeneficiarySourcePropertyModel(self, beneficiarySource,properties):
        beneficiarySourcePropertyModels = []        
        for property in properties:
            modelType = dict({'beneficiarySource':beneficiarySource,'propertyType':property['propertyType'],'propertyValue':property['propertyValue']})
            beneficiarySourcePropertyModels.append(modelType)
        
        return beneficiarySourcePropertyModels
            
    def SaveBeneficiarySourceProperty(self, beneficiarySourcePropertyModels):
        created = []
        for beneficiarySourcePropertyModel in beneficiarySourcePropertyModels:
            data = self.data.beneficiarySourcePropertyRepository.create(beneficiarySourcePropertyModel);
            created.append(data)
        return created