from django.db import IntegrityError
from DataAccessLayer.FundingSourceType.model import FundingSourceType as FundingSourceTypeModel
from DataAccessLayer.FundingSourceType.repository import FundingSourceTypeRepository
from DataAccessLayer.FundingSourceType.serializer import FundingSourceTypeSerializer
from DataAccessLayer.DataModule import DataModule
from Utility.Response import Response
from Utility.Utility import Utility
from Utility.logger import Logger
import uuid

class FundingSourceTypeService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.FundingSourceTypeService')
        self.requestId = uuid.uuid4()

    def createFundingSourceType(self, data):
        try:
            validData = FundingSourceTypeSerializer(data=data)

            if not validData.is_valid():
                self.logger.Info(r"Create Funding Source Type. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), self.requestId))
                return Response.error(self.requestId, error=validData.errors),400

            formattedData = Utility.convertFieldValueToLowerCase(data, 'name')
            savedData = self.data.fundingSourceTypeRepository.create(formattedData)
            self.logger.Info(r"Funding  Source Type With Id --> {} was successfully created, n\ REQUESTID => {}".format(FundingSourceTypeSerializer(savedData).data['id'], self.requestId))
            return Response.success(self.requestId, data=FundingSourceTypeSerializer(savedData).data),201
        
        except IntegrityError:
            self.logger.Info(r"Funding Source Type with name --> {} was not created. Funding Source Type already exists. n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.error(self.requestId, error=r"{} Funding Source Type already exists".format(data['name']), responseCode='01'),409

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type --> {} could not be created, n\ REQUESTID => {}".format(str(data), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500

    def getAllFundingSourceTypes(self):
        try:
            data = self.data.fundingSourceTypeRepository.getAll()
            self.logger.Info(r"Successfully got all Funding Source Types, n\ REQUESTID => {}".format(self.requestId))
            return Response.success(self.requestId, data=FundingSourceTypeSerializer(data, many=True).data),200

        except BaseException as ex:
            self.logger.Info(r"Funding Source Types could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
    
    def getOneFundingSourceType(self, pk):
        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist"),404

            data = self.data.fundingSourceTypeRepository.getOne(pk)
            self.logger.Info(r"Successfully got Funding Source Type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.success(self.requestId, data=FundingSourceTypeSerializer(data).data),200
            
        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(
                pk, str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500


    def updateFundingSourceType(self, pk, dataToUpdate):
        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist"), 404

            updatedData = self.data.fundingSourceTypeRepository.update(dataToUpdate, pk)
            self.logger.Info(r"Successfully updated funding source type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.success(self.requestId, message='Funding Source Type has been successfully updated', data=FundingSourceTypeSerializer(updatedData).data),200

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be updated. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500

    def deleteFundingSourceType(self, pk):
        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist"),404
                
            deletedData = self.data.fundingSourceTypeRepository.delete(pk)
            if deletedData > 0 :
                self.logger.Info(r"Successfully deleted funding source type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.success(self.requestId, message="Funding Group Type is successfully deleted"),200

            self.logger.Info(r"Funding Source Type with id --> {} could not be deleted. n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.error(self.requestId, message="Please try again later"),400

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be deleted. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
