from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from LogicLayer.FundingSourceType.service import FundingSourceTypeService as service
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.FundingSourceType.FundingSourceTypeResponseSerializer import (swaggerFieldSchema, FundingSourceTypeDeleteResponse, 
FundingSourceTypeGetResponse, FundingSourceTypePostResponse, FundingSourceTypeUpdateResponse, FundingSourceTypeGetOneResponse)
from Utility.Response import Response as ResponseWrapper
from Utility.Utility import Utility
from Utility.middlewares.validateUserRole import ValidateUserRole
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer

class FundingSourceTypeList(APIView):
    def __init__(self):
        self.fundingSourceTypeService = service()

    @swagger_auto_schema(responses={201: FundingSourceTypePostResponse, 400 : ErrorResponseSerializer,409 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        response, status = self.fundingSourceTypeService.createFundingSourceType(request.data)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: FundingSourceTypeGetResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer })
    def get(self, request,format=None):
        response, status = self.fundingSourceTypeService.getAllFundingSourceTypes()
        return Response(response, status=status)


class FundingSourceTypeDetail(APIView):
    def __init__(self):
        self.fundingSourceTypeService = service()
        self.logger = Logger('LogicLayer.FundingSourceTypeList')

    @swagger_auto_schema(responses={200: FundingSourceTypeGetOneResponse, 400 :ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self, request, pk,format=None):
        response, status = self.fundingSourceTypeService.getOneFundingSourceType(pk)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: FundingSourceTypeUpdateResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    @method_decorator(ValidateUserRole)
    def put(self, request, pk, format=None):
        response, status = self.fundingSourceTypeService.updateFundingSourceType(pk, request.data)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: FundingSourceTypeDeleteResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    @method_decorator(ValidateUserRole)
    def delete(self, request, pk, format=None):
        response, status = self.fundingSourceTypeService.deleteFundingSourceType(pk)
        return Response(response, status=status)
