from django.db import IntegrityError
from django.utils import timezone
from DataAccessLayer.FundingGroupType.model import FundingGroupType as fundingGroupTypeModel
from DataAccessLayer.FundingGroupType.repository import FundingGroupTypeRepository as fundingGroupTypeRepo
from DataAccessLayer.FundingGroupType.serializer import FundingGroupTypeSerializer
from Utility.Response import Response
from Utility.logger import Logger
from Utility.Utility import Utility

import uuid
class FundingGroupTypeService:
    def __init__(self):
        self.fundingGroupTypeRepository = fundingGroupTypeRepo(fundingGroupTypeModel)
        self.logger = Logger('LogicLayer.FundingGroupTypeService')

    def createFundingGroupType(self, data):
        requestId = uuid.uuid4()

        try:
            savedData = self.fundingGroupTypeRepository.create(data)
            self.logger.Info(r"Funding Group Type with id --> {} was successfully created, n\ REQUESTID => {}".format(FundingGroupTypeSerializer(savedData).data['id'], requestId))
            return Response.success(requestId, data=FundingGroupTypeSerializer(savedData).data)

        except Exception:
            self.logger.Info(r"Funding Group Type --> {} could not be created, n\ REQUESTID => {}".format(str(data), requestId))
            return Response.error(requestId, error=str(Exception))

    def getAllFundingGroupType(self):
        requestId = uuid.uuid4()

        try:
            data = self.fundingGroupTypeRepository.getAll()
            self.logger.Info(r"Successfully got all funding group types, n\ REQUESTID => {}".format(requestId))
            return Response.success(requestId, data=FundingGroupTypeSerializer(data, many=True).data)

        except Exception:
            self.logger.Info(r"Funding Group Types could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))
    
    def getOneFundingGroupType(self,pk):
        requestId = uuid.uuid4()

        try:
            if self.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist", responseCode='03')

            data = self.fundingGroupTypeRepository.getOne(pk)
            self.logger.Info(r"Successfully got funding group type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
            return Response.success(requestId, data=FundingGroupTypeSerializer(data).data)

        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))


    def updateFundingGroupType(self, pk, dataToUpdate):
        requestId = uuid.uuid4()

        try:
            requestBody = dataToUpdate

            if 'name' in dataToUpdate: requestBody = Utility.convertFieldValueToLowerCase(dataToUpdate, 'name')
            modifiedData = Utility.appendNewFieldToDict(requestBody, 'updatedAt', timezone.now())

            if self.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist", responseCode='03')

            updatedData = self.fundingGroupTypeRepository.update(modifiedData, pk)
            self.logger.Info(r"Successfully updated funding group type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
            return Response.success(requestId, message='Funding Group Type has been successfully updated', data=[{ "count": updatedData}])

        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be updated. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))

    def deleteFundingGroupType(self, pk):
        requestId = uuid.uuid4()

        try:
            if self.fundingGroupTypeRepository.IsExists(pk) is False:
                self.logger.Info(r"Funding Group Type with id --> {} does not exist, n\ REQUESTID => {}".format(pk, requestId))
                return Response.error(requestId, message="Funding Group Type does not exist", responseCode='03')

            deletedData = self.fundingGroupTypeRepository.delete(pk)
            if deletedData > 0 :
                self.logger.Info(r"Successfully deleted funding group type with id --> {}, n\ REQUESTID => {}".format(pk, requestId))
                return Response.success(requestId, message="Funding Group Type is successfully deleted", data=[{ "count": deletedData}])

            self.logger.Info(r"Funding Group Type with id --> {} could not be deleted. n\ REQUESTID => {}".format(pk, requestId))
            return Response.error(requestId, message="Please try again later")
            
        except Exception:
            self.logger.Info(r"Funding Group Type with id --> {} could not be deleted. An exception occured: {}, n\ REQUESTID => {}".format(pk, str(Exception), requestId))
            return Response.error(requestId, error=str(Exception))
        