from Utility.logger import Logger
from Utility.Response import Response
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
from DataAccessLayer.DataModule import DataModule
import uuid
from django.db import IntegrityError


class BeneficiarySourceTypeService:
    def __init__(self):
        self.logger = Logger('LogicLayer.BeneficiarySourceTypeService')
        self.data = DataModule()


    def getAllBeneficiarySourceType(self):

        requestId = uuid.uuid4()
        try:
            data = self.data.beneficiarySourceTypeRepository.getAll()
            responseData = BeneficiarySourceTypeSerializer(data,many=True).data
            self.logger.Info("REQUESTID => {} MESSAGE => Beneficiary source type gotten successfully".format(requestId))
        except Exception as ex:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId),500
        
        return Response.success(requestId,data=responseData),200


    def updateBeneficiarySourceType(self,data,primaryKey):

        requestId = uuid.uuid4()
        try:
            validData = BeneficiarySourceTypeSerializer(data=data)
            if(validData.is_valid() is False): Response.error(requestId,message="Validation Error",responseCode="01",error=validData.errors),400

            if(self.data.beneficiarySourceTypeRepository.IsExists(primaryKey) is False):
                self.logger.Info(r"REQUESTID => {}Beneficiary source type doesn't exist.".format(requestId))
                return  Response.error(requestId,"Beneficiary source type doesn't exist.",responseCode="03"),404 

            updatedRowCount = self.data.beneficiarySourceTypeRepository.update(validData.data,primaryKey)
            if updatedRowCount is None: 
                self.logger.Info(r"""REQUESTID => {} n\ Beneficiary source type with ID => {} could not be updated.""".format(requestId,primaryKey))
                return Response.error(requestId,"Update not successful. Please try again later.",responseCode="03"),204
            
            message = "Beneficiary source type has been updated successfully"
            self.logger.Info(r"""REQUESTID => {} n\ {}. n\  ID => {} """.format(requestId, message, primaryKey))
        
        except IntegrityError:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,IntegrityError))
            return Response.error(requestId,message="Name already exists",responseCode="01"),409

        except Exception as ex:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId),500
            
        return Response.success(requestId,data=BeneficiarySourceTypeSerializer(updatedRowCount).data),200


    def createBeneficiarySourceType(self,data):

        requestId = uuid.uuid4()
        try:
            validData = BeneficiarySourceTypeSerializer(data=data)
            if(validData.is_valid() is False): return Response.error(requestId,message="Validation Error",responseCode="01",error=validData.errors),400
            
            savedData = self.data.beneficiarySourceTypeRepository.create(validData.data)
            responseData = BeneficiarySourceTypeSerializer(savedData,many=False).data
            message = "Beneficiary source type created successfully"
            self.logger.Info(r"""REQUESTID => {} n\ {}.""".format(requestId,message))

        except IntegrityError:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,IntegrityError))
            return Response.error(requestId,message="Name already exists",responseCode="01"),409

        except Exception as ex:
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId),500
        
        return Response.success(requestId,message=message,data=responseData),201

    
    def deleteBeneficiarySourceType(self, primaryKey):
        requestId = uuid.uuid4()
        try:
            if(self.data.beneficiarySourceTypeRepository.IsExists(primaryKey) is False):
                self.logger.Info(r"REQUESTID => {}Beneficiary source type doesn't exist.".format(requestId))
                return  Response.error(requestId,"Beneficiary source type doesn't exist.",responseCode="03"),404
            
            deletedRowCount = self.data.beneficiarySourceTypeRepository.delete(primaryKey);

            if deletedRowCount <= 0 : 
                self.logger.Info(r"""REQUESTID => {} n\ Beneficiary source type with ID => {} could not be deleted.""".format(requestId,primaryKey))
                return Response.error(requestId,"Delete not successful. Please try again later.",responseCode="03"),204
            
            message = "Beneficiary source type has been deleted successfully"
            self.logger.Info(r"""REQUESTID => {} n\ {}. n\  ID => {} """.format(requestId, message, primaryKey))
            
        except Exception as ex :
            self.logger.Error("RequestID =>{} ERROR => {}".format(requestId,ex))
            return Response.error(requestId),500
        
        return Response.success(requestId,data=message),200