from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from LogicLayer.FundingGroupType.service import FundingGroupTypeService as service
from Utility.middlewares.validateUserRole import ValidateUserRole
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer
from DataAccessLayer.FundingGroupType.serializer import FundingGroupTypeSerializer
from Utility.Documentation.FundingGroupType.FundingGroupTypeResponseSerializer import (swaggerFieldSchema, FundingGroupTypeDeleteResponse, 
FundingGroupTypeGetResponse, FundingGroupTypePostResponse, FundingGroupTypeUpdateResponse, FundingGroupTypeGetOneResponse)

class FundingGroupTypeList(APIView):
    def __init__(self):
        self.fundingGroupTypeService = service()

    @swagger_auto_schema(responses={201: FundingGroupTypePostResponse, 400 : ErrorResponseSerializer,409 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer},request_body=FundingGroupTypeSerializer)
    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        response, status = self.fundingGroupTypeService.createFundingGroupType(request.data)
        return Response(response, status=status)

    @swagger_auto_schema(responses={200: FundingGroupTypeGetResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer })
    def get(self,request,format=None):
        response, status = self.fundingGroupTypeService.getAllFundingGroupType()
        return Response(response, status=status)

class FundingGroupTypeDetail(APIView):
    def __init__(self):
        self.fundingGroupTypeService = service()

    @swagger_auto_schema(responses={200: FundingGroupTypeGetOneResponse, 400 :ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self, request, pk, format=None):
        response, status = self.fundingGroupTypeService.getOneFundingGroupType(pk)
        return Response(response, status)

    @swagger_auto_schema(responses={200: FundingGroupTypeUpdateResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    @method_decorator(ValidateUserRole)
    def put(self, request, pk, format=None):
        response, status = self.fundingGroupTypeService.updateFundingGroupType(pk, request.data)
        return Response(response, status)
    
    @swagger_auto_schema(responses={200: FundingGroupTypeDeleteResponse, 400 : ErrorResponseSerializer,500 : ServerErrorResponseSerializer})
    @method_decorator(ValidateUserRole)
    def delete(self, request, pk, format=None):
        response, status = self.fundingGroupTypeService.deleteFundingGroupType(pk)
        return Response(response, status)
    