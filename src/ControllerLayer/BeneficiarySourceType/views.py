import uuid
from django.utils.decorators import method_decorator
from Utility.middlewares.validateUserRole import ValidateUserRole
from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.LogicModule import LogicModule
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.BeneficiarySourceType.ResponseSerializer import BST_GetResponseSerializer,BST_PostResponseSerializer,BST_UpdateResponseSerializer,BST_DeleteResponseSerializer
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer

class BeneficiarySourceTypeList(APIView):
    def __init__(self):
        self.logic = LogicModule()

    
    @swagger_auto_schema(responses={200: BST_GetResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self,request,format=None):
        data,status = self.logic.beneficiarySourceTypeService.getAllBeneficiarySourceType()
        return Response(data,status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={201: BST_PostResponseSerializer,401 : ErrorResponseSerializer,409 : ErrorResponseSerializer,500:ServerErrorResponseSerializer},request_body=BeneficiarySourceTypeSerializer(fields=('updatedAt',)))
    def post(self, request, format=None):        
        data,status = self.logic.beneficiarySourceTypeService.createBeneficiarySourceType(request.data)
        return Response(data, status)


class BeneficiarySourceTypeDetail(APIView):
    def __init__(self):
        self.logic = LogicModule()

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: BST_UpdateResponseSerializer,404 : ErrorResponseSerializer,409:ErrorResponseSerializer,500:ServerErrorResponseSerializer})
    def put(self, request, pk, format=None):        
        data,status = self.logic.beneficiarySourceTypeService.updateBeneficiarySourceType(request.data,pk)
        return Response(data,status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: BST_DeleteResponseSerializer,404 :ErrorResponseSerializer,500: ServerErrorResponseSerializer})
    def delete(self, request, pk, format=None):
        data,status = self.logic.beneficiarySourceTypeService.deleteBeneficiarySourceType(pk)
        return Response(data,status=status)

    
    