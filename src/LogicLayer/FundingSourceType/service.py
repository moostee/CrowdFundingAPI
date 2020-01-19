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

    def createFundingSourceType(self, data):
        requestId = uuid.uuid4()
        try:
            validData = FundingSourceTypeSerializer(data=data)

            if not validData.is_valid():
                self.logger.Info(r"Create Funding Source Type. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), requestId))
                return Response.error(requestId, error=validData.errors), 400

            formattedData = Utility.convertFieldValueToLowerCase(data, 'name')
            savedData = self.data.fundingSourceTypeRepository.create(formattedData)
            self.logger.Info(r"Funding  Source Type With Id --> {} was successfully created, n\ REQUESTID => {}".format(FundingSourceTypeSerializer(savedData).data['id'], requestId))
            return Response.success(requestId, data=FundingSourceTypeSerializer(savedData).data), 201
        
        except IntegrityError:
            self.logger.Info(r"Funding Source Type with name --> {} was not created. Funding Source Type already exists. n\ REQUESTID => {}".format(data['name'],requestId))
            return Response.error(requestId, error=r"{} Funding Source Type already exists".format(data['name']), responseCode='01'), 409

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type --> {} could not be created, n\ REQUESTID => {}".format(str(data), requestId))
            return Response.error(requestId, error=str(ex)), 400

    def getAllFundingSourceTypes(self):
        requestId = uuid.uuid4()

        try:
            data = self.data.fundingSourceTypeRepository.getAll()
            self.logger.Info(r"Successfully got all Funding Source Types, n\ REQUESTID => {}".format(requestId))
            return Response.success(requestId, data=FundingSourceTypeSerializer(data, many=True).data), 200

        except BaseException as ex:
            self.logger.Info(r"Funding Source Types could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(
                str(ex), requestId))
            return Response.error(requestId, error=str(ex)), 400
    
    def getOneFundingSourceType(self, pk):
        requestId = uuid.uuid4()

        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist"), 400

            data = self.data.fundingSourceTypeRepository.getOne(pk)
            self.logger.Info(r"Successfully got Funding Source Type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
            return Response.success(requestId, data=FundingSourceTypeSerializer(data).data), 200
            
        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(
                pk, str(ex), requestId))
            return Response.error(requestId, error=str(ex)), 400


    def updateFundingSourceType(self, pk, dataToUpdate):
        requestId = uuid.uuid4()

        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist"), 400

            updatedData = self.data.fundingSourceTypeRepository.update(dataToUpdate, pk)
            self.logger.Info(r"Successfully updated funding source type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
            print('1 ================>', updatedData)
            return Response.success(requestId, message='Funding Source Type has been successfully updated', data=FundingSourceTypeSerializer(updatedData).data), 200

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be updated. An exception occured: {}, n\ REQUESTID => {}".format(
                pk, str(ex), requestId))
            return Response.error(requestId, error=str(ex)), 400

    def deleteFundingSourceType(self, pk):
        requestId = uuid.uuid4()

        try:
            if self.data.fundingSourceTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Source Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist"), 400
                
            deletedData = self.data.fundingSourceTypeRepository.delete(pk)
            if deletedData > 0 :
                self.logger.Info(r"Successfully deleted funding source type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
                return Response.success(requestId, message="Funding Group Type is successfully deleted"), 200

            self.logger.Info(r"Funding Source Type with id --> {} could not be deleted. n\ REQUESTID => {}".format(
                pk, requestId))
            return Response.error(requestId, message="Please try again later"), 400

        except BaseException as ex:
            self.logger.Info(r"Funding Source Type with id --> {} could not be deleted. An exception occured: {}, n\ REQUESTID => {}".format(
                pk, str(ex), requestId))
            return Response.error(requestId, error=str(ex)), 400
