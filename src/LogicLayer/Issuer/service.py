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
            formattedData = {key:(value.lower() if type(value) == str else value) for key,value in data.items()}
            savedIssuer = self.data.issuerRepository.create(formattedData)
            self.logger.Info(r"Issuer with name --> {} was successfully created, n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.success(self.requestId, data=IssuerSerializer(savedIssuer,many=False).data)
        except IntegrityError:
            self.logger.Info(r"Issuer with name --> {} was not created. Issuer already exist. n\ REQUESTID => {}".format(data['name'],self.requestId))
            return Response.error(self.requestId, error=r"{} issuer already exist".format(data['name']))
        except BaseException as ex:
            self.logger.Info(r"Issuer with name --> {} was not created. An exception occured: {}, n\ REQUESTID => {}".format(data['name'],str(ex),self.requestId))
            return Response.error(self.requestId, error=str(ex))

    def getAllIssuers(self):
        try:
            issuers = self.data.issuerRepository.getAll()
            self.logger.Info(r"Successfully got all issuers, n\ REQUESTID => {}".format(self.requestId))
            return Response.success(self.requestId, data=IssuerSerializer(issuers, many=True).data)

        except BaseException as ex:
            self.logger.Info(r"Issuers could not be retrieved. An exception occured: {}, n\ REQUESTID => {}".format(str(ex), self.requestId))
            return Response.error(self.requestId, error=str(ex))
