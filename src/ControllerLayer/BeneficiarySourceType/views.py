import uuid
from django.utils.decorators import method_decorator
from Utility.middlewares.validateUserRole import ValidateUserRole
from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.LogicModule import LogicModule
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.BeneficiarySourceType.ResponseSerializer import GetResponseSerializer,PostResponseSerializer,UpdateResponseSerializer,DeleteResponseSerializer

class BeneficiarySourceTypeList(APIView):
    def __init__(self):
        self.logic = LogicModule()

    
    @swagger_auto_schema(responses={200: GetResponseSerializer,500 : "An error occured while processing your request. Please try again later"})
    def get(self,request,format=None):
        data,status = self.logic.beneficiarySourceTypeService.getAllBeneficiarySourceType()
        return Response(data,status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={201: PostResponseSerializer,401 : "Bad Request",409 : "Resource conflict",500: "An error occured while processing your request. Please try again later"},request_body=BeneficiarySourceTypeSerializer(fields=('name')))
    def post(self, request, format=None):
        validData = BeneficiarySourceTypeSerializer(data=request.data)
        if(validData.is_valid(raise_exception=True) is False): return Response(validData.errors)
        data,status = self.logic.beneficiarySourceTypeService.createBeneficiarySourceType(validData.data)
        return Response(data, status)


class BeneficiarySourceTypeDetail(APIView):
    def __init__(self):
        self.logic = LogicModule()

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: UpdateResponseSerializer,404 : "Resource not found",409:"Resource conflict",500: "An error occured while processing your request. Please try again later"})
    def put(self, request, pk, format=None):
        validData = BeneficiarySourceTypeSerializer(data=request.data)
        if(validData.is_valid(raise_exception=True) is False): return Response(validData.errors)
        data,status = self.logic.beneficiarySourceTypeService.updateBeneficiarySourceType(validData.data,pk)
        return Response(data,status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: DeleteResponseSerializer,404 : "Resource not found",500: "An error occured while processing your request. Please try again later"})
    def delete(self, request, pk, format=None):
        data,status = self.logic.beneficiarySourceTypeService.deleteBeneficiarySourceType(pk)
        return Response(data,status=status)

    
    