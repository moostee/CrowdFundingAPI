from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.Issuer.service import IssuerService as service
from DataAccessLayer.Issuer.serializer import IssuerSerializer
from Utility.Response import Response as ResponseWrapper
from Utility.logger import Logger
from Utility.middlewares.validateUserRole import ValidateUserRole
from django.utils.decorators import method_decorator
import uuid

class Issuer(APIView):
    def __init__(self):
        self.logger = Logger('ControllerLayer.Issuer')
        self.IssuerService = service()
        self.requestId = uuid.uuid4()

    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        validData = IssuerSerializer(data=request.data)
        if not validData.is_valid():
            self.logger.Info(r"Create Issuer. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), self.requestId))
            return Response(ResponseWrapper.error(self.requestId, message="Validation error occured processing request", error=validData.errors, responseCode='01'))
        return Response(self.IssuerService.createIssuer(validData.data))
    
    def get(self, request, format=None):
        return Response(self.IssuerService.getAllIssuers())
