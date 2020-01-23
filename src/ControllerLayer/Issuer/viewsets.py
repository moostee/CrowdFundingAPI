from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.Issuer.service import IssuerService as service
from Utility.middlewares.validateUserRole import ValidateUserRole
from django.utils.decorators import method_decorator

class Issuer(APIView):
    def __init__(self):
        self.IssuerService = service()

    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        response,status = self.IssuerService.createIssuer(request.data)
        return Response(response, status=status)

    def get(self, request, format=None):
        response,status = self.IssuerService.getAllIssuers()
        return Response(response, status=status)

class IssuerDetails(APIView):
    def __init__(self):
        self.IssuerService = service()
    
    def get(self, request, pk, format=None):
        response,status = self.IssuerService.getOneIssuer(pk)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    def put(self, request, pk, format=None):
        response,status = self.IssuerService.updateIssuer(request.data, pk)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    def delete(self, request, pk, format=None):
        response,status = self.IssuerService.deleteIssuer(pk)
        return Response(response, status=status)
