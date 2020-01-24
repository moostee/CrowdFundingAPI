import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.LogicModule import LogicModule
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.BeneficiarySourceType.ResponseSerializer import GetResponseSerializer,PostResponseSerializer,UpdateResponseSerializer,DeleteResponseSerializer

class BeneficiarySourceTypeList(APIView):
    def __init__(self):
        self.logic = LogicModule()

    @swagger_auto_schema(responses={200: GetResponseSerializer})
    def get(self,request,format=None):
        return Response(self.logic.beneficiarySourceTypeService.getAllBeneficiarySourceType());

    @swagger_auto_schema(responses={200: PostResponseSerializer,401 : "Bad Request"},request_body=BeneficiarySourceTypeSerializer(fields=('name')))
    def post(self, request, format=None):
        validData = BeneficiarySourceTypeSerializer(data=request.data)
        if(validData.is_valid(raise_exception=True) is False): return Response(validData.errors)
        return Response(self.logic.beneficiarySourceTypeService.createBeneficiarySourceType(validData.data))


class BeneficiarySourceTypeDetail(APIView):
    def __init__(self):
        self.logic = LogicModule()


    @swagger_auto_schema(responses={200: UpdateResponseSerializer})
    def put(self, request, pk, format=None):
        validData = BeneficiarySourceTypeSerializer(data=request.data)
        if(validData.is_valid(raise_exception=True) is False): return Response(validData.errors)
        return Response(self.logic.beneficiarySourceTypeService.updateBeneficiarySourceType(validData.data,pk))


    @swagger_auto_schema(responses={200: DeleteResponseSerializer})
    def delete(self, request, pk, format=None):
        return Response(self.logic.beneficiarySourceTypeService.deleteBeneficiarySourceType(pk))

    
    