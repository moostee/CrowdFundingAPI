from DataAccessLayer.DataModule import DataModule
from DataAccessLayer.Issuer.serializer import IssuerSerializer
from Utility.Response import Response
from Utility.logger import Logger
from Utility.Utility import Utility
from django.db import IntegrityError

import uuid

class IssuerService:
    def __init__(self):
        self.data = DataModule()
        self.logger = Logger('LogicLayer.IssuerService')
        self.requestId = uuid.uuid4()
    
    def createIssuer(self,data):
        try:
            validData = IssuerSerializer(data=data)
            if not validData.is_valid():
                self.logger.Info(r"Issuer with data \"{}\" could not be validated  with error {} n\ REQUESTID => {}".format(data,validData.errors,self.requestId))
                return Response.error(self.requestId, error=validData.errors, responseCode='01'),400
            savedIssuer = self.data.issuerRepository.create(data)
            self.logger.Info(r"Issuer with name --> {} was successfully created, n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.success(self.requestId, data=IssuerSerializer(savedIssuer,many=False).data),201
        except IntegrityError:
            self.logger.Info(r"Issuer with name --> {} was not created. Issuer already exist. n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.error(self.requestId, error=r"{} issuer already exist".format(data['name']), responseCode='01'),409
        except BaseException as ex:
            self.logger.Info(r"Issuer with name --> {} was not created. An exception occured: {}, n\ REQUESTID => {}".format(data['name'],str(ex),self.requestId))
            return Response.error(self.requestId, error=str(ex)),500

    def getAllIssuers(self):
        try:
            issuers = self.data.issuerRepository.getAll()
            self.logger.Info(r"Successfully got all issuers, n\ REQUESTID => {}".format(self.requestId))
            return Response.success(self.requestId, data=IssuerSerializer(issuers, many=True).data),200

        except BaseException as ex:
            self.logger.Info(r"Issuers could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
 
    def getOneIssuer(self,pk):
        try:
            if self.data.issuerRepository.IsExists(pk):
                issuer = self.data.issuerRepository.getOne(pk)
                self.logger.Info(r"Successfully got issuer {}, n\ REQUESTID => {}".format(issuer.name,self.requestId))
                return Response.success(self.requestId, data=IssuerSerializer(issuer, many=False).data),200
            else:
                self.logger.Info(r"Issuer with id {} does not exist, n\ REQUESTID => {}".format(pk,self.requestId))
                return Response.error(self.requestId, message=r"Issuer with id {} does not exist.".format(pk)),404
        
        except BaseException as ex:
            self.logger.Info(r"Issuers could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
    

    def updateIssuer(self, data, pk):
        try:
            if self.data.issuerRepository.IsExists(pk):
                formattedData = {key:(value.lower() if type(value) == str else value) for key,value in data.items()}
                updatedIssuer = self.data.issuerRepository.update(formattedData, pk)
                self.logger.Info(r"Successfully updated issuer: ID --> {} with {}, requestId --> {}".format(pk,data,self.requestId)),200
                return Response.success(self.requestId, data=IssuerSerializer(updatedIssuer, many=False).data, message="Issuer successfully updated")
            else:
                self.logger.Info(r"Issuer with id --> {} was not found, requestId --> {}".format(pk, self.requestId))
                return Response.error(self.requestId, error=r"Issuer with id {} does not exist".format(pk), responseCode="03"),404
        except BaseException as ex:
            self.logger.Info(r"Unable to update issuer with id --> {} due to exception--> {}, requestId --> {}".format(pk, str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
    
    def deleteIssuer(self, pk):
        try:
            if self.data.issuerRepository.IsExists(pk):
                self.data.issuerRepository.delete(pk)
                self.logger.Info(r"Successfully deleted issuer with id --> {}, requestId --> {}".format(pk,self.requestId))
                return Response.success(self.requestId, message="Issuer was successfully deleted"),200
            else:
                self.logger.Info(r"Issuer with id --> {} was not found, requestId --> {}".format(pk,self.requestId))
                return Response.error(self.requestId, error="Issuer does not found", responseCode="03"),404
        except BaseException as ex:
            self.logger.Info(r"Unable to delete issuer with id --> {} due to exception--> {}, requestId --> {}".format(pk, str(ex),self.requestId))
            return Response.error(self.requestId, error=str(ex)),500
