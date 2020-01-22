import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from LogicLayer.Funding.service import FundingService as service
from DataAccessLayer.Funding.serializer import FundingSerializer
from Utility.Utility import Utility
from Utility.middlewares.validateUserRole import ValidateUserRole
from Utility.Documentation.Funding.FundingResponseSerializer import swaggerFieldSchema, FundingPostResponseSerializer, FundingGetResponseSerializer

class FundingList(APIView):
    def __init__(self):
        self.FundingService = service()

    @swagger_auto_schema(responses={201: FundingPostResponseSerializer, 400 : "Bad Request"},
    request_body=FundingSerializer(fields=swaggerFieldSchema))
    def post(self, request, format=None):
        response, status = self.FundingService.createFunding(request.data)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: FundingGetResponseSerializer})
    @method_decorator(ValidateUserRole)
    def get(self, request, format=None):
        response, status = self.FundingService.getAllFundings()
        return Response(response, status=status)
    