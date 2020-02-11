from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.Issuer.service import IssuerService as service
from Utility.middlewares.validateUserRole import ValidateUserRole
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from DataAccessLayer.Issuer.serializer import IssuerSerializer
from Utility.Documentation.Issuer.IssuerResponseSerializer import GetOneIssuerResponseSerializer, GetIssuerResponseSerializer, PostIssuerResponseSerializer, UpdateIssuerResponseSerializer, DeleteIssuerResponseSerializer
from Utility.Documentation.Issuer.IssuerRequestSerializer import IssuerRequestSerializer
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer

class Issuer(APIView):
    def __init__(self):
        self.IssuerService = service()

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={201: PostIssuerResponseSerializer,400 : ErrorResponseSerializer,401 : ErrorResponseSerializer,409 : ErrorResponseSerializer,500:ServerErrorResponseSerializer},request_body=IssuerRequestSerializer())
    def post(self, request, format=None):
        response,status = self.IssuerService.createIssuer(request.data)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: GetIssuerResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self, request, format=None):
        response,status = self.IssuerService.getAllIssuers()
        return Response(response, status=status)

class IssuerDetails(APIView):
    def __init__(self):
        self.IssuerService = service()
    
    @swagger_auto_schema(responses={200: GetOneIssuerResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self, request, pk, format=None):
        response,status = self.IssuerService.getOneIssuer(pk)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: UpdateIssuerResponseSerializer,404 : ErrorResponseSerializer,500:ServerErrorResponseSerializer})
    def put(self, request, pk, format=None):
        response,status = self.IssuerService.updateIssuer(request.data, pk)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: DeleteIssuerResponseSerializer,404 : ErrorResponseSerializer,500:ServerErrorResponseSerializer})
    def delete(self, request, pk, format=None):
        response,status = self.IssuerService.deleteIssuer(pk)
        return Response(response, status=status)
