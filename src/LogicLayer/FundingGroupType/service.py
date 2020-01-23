from django.db import IntegrityError
from django.utils import timezone
from DataAccessLayer.FundingGroupType.model import FundingGroupType as fundingGroupTypeModel
from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.FundingGroupType.serializer import FundingGroupTypeSerializer
from Utility.Response import Response
from Utility.logger import Logger
from Utility.Utility import Utility

import uuid
class FundingGroupTypeService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.FundingGroupTypeService')
        self.requestId = uuid.uuid4()

    def createFundingGroupType(self, data):
        try:
            validData = FundingGroupTypeSerializer(data=data)

            if(validData.is_valid() is False):
                self.logger.Info(r"Create Funding Group Type. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), self.requestId))
                return Response.error(self.requestId, error=validData.errors, responseCode='01'), 400

            savedData = self.data.fundingGroupTypeRepository.create(data)
            self.logger.Info(r"Funding Group Type with id --> {} was successfully created, n\ self.requestId => {}".format(FundingGroupTypeSerializer(savedData).data['id'], self.requestId))
            return Response.success(self.requestId, data=FundingGroupTypeSerializer(savedData).data), 201
        
        except IntegrityError:
            self.logger.Info(r"Funding Group Type with name --> {} was not created. Funding Group Type already exists. n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.error(self.requestId, error=r"{} Funding Group Type already exists".format(data['name']), responseCode='01'), 409

        except BaseException as ex:
            self.logger.Info(r"Funding Group Type --> {} could not be created, n\ REQUESTID => {}".format(str(data), self.requestId))
            return Response.error(self.requestId, error=str(ex)), 400

    def getAllFundingGroupType(self):
        try:
            data = self.data.fundingGroupTypeRepository.getAll()
            self.logger.Info(r"Successfully got all funding group types, n\ REQUESTID => {}".format(self.requestId))
            return Response.success(self.requestId, data=FundingGroupTypeSerializer(data, many=True).data), 200

        except Exception:
            self.logger.Info(r"Funding Group Types could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(Exception), self.requestId))
            return Response.error(self.requestId, error=str(Exception)), 400
    
    def getOneFundingGroupType(self,pk):
        try:
            if self.data.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist", responseCode='03'), 404

            data = self.data.fundingGroupTypeRepository.getOne(pk)
            self.logger.Info(r"Successfully got funding group type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.success(self.requestId, data=FundingGroupTypeSerializer(data).data), 200

        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), self.requestId))
            return Response.error(self.requestId, error=str(Exception)), 400


    def updateFundingGroupType(self, pk, dataToUpdate):
        try:
            if self.data.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist", responseCode='03'), 404

            updatedData = self.data.fundingGroupTypeRepository.update(dataToUpdate, pk)
            self.logger.Info(r"Successfully updated funding group type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.success(self.requestId, message='Funding Group Type has been successfully updated', data=FundingGroupTypeSerializer(updatedData, many=False).data), 200

        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be updated. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), self.requestId))
            return Response.error(self.requestId, error=str(Exception)), 400

    def deleteFundingGroupType(self, pk):
        try:
            if self.data.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.error(self.requestId, message="Funding Group Type does not exist", responseCode='03'), 404

            deletedData = self.data.fundingGroupTypeRepository.delete(pk)
            if deletedData > 0 :
                self.logger.Info(r"Successfully deleted funding group type with id --> {}, n\ REQUESTID => {}".format(pk, self.requestId))
                return Response.success(self.requestId, message="Funding Group Type is successfully deleted", data=[{ "count": deletedData}]), 200

            self.logger.Info(r"Funding Group Type with id --> {} could not be deleted. n\ REQUESTID => {}".format(pk, self.requestId))
            return Response.error(self.requestId, message="Please try again later"), 400
            
        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be deleted. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), self.requestId))
            return Response.error(self.requestId, error=str(Exception)), 400
        