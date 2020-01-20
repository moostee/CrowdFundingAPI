from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.FundingSource.serializer import FundingSourceSerializer
from Utility.Response import Response
import uuid
import json
from Utility.logger import Logger

class FundingSourceService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.FundingSourceService')
    
    def getFundingSourcesForUser(self,userId):
        fieldsToReturn = ('id','sourceNumber','userId','issuerId','fundingSourceTypeId')
        try:
            requestId = uuid.uuid4();
            if self.data.fundingSourceRepository.HasFundingSource(userId) is False:
                self.logger.Info("User -->{0}does not have a funding, n\ REQUESTID =>{1}".format(userId,requestId))
                return Response.unSuccessfulResponse(requestId,"User does not have any funding source")
            
            userFundingSource = self.data.fundingSourceRepository.GetUserFundingSource(userId)
            print('-->',type(userFundingSource))
            responseData = FundingSourceSerializer(userFundingSource,many=True,fields=fieldsToReturn).data
            print('--->',type(responseData))
            self.logger.Info("Successfully got funding for user {0},n\ REQUESTID => {1}".format(userId,requestId))

        except Exception as exception :
            self.logger.Error(exception)
            return Response.ExceptionResponse(requestId)
        
        return Response.successfulResponse(requestId,data=responseData)


    