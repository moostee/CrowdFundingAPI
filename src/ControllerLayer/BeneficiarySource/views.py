from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.LogicModule import LogicModule
from DataAccessLayer.BeneficiarySource.serializer import BeneficiarySourceSerializer,CreateBeneficiarySourceSerializer
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.BeneficiarySource.ResponseSerializer import BS_GetResponseSerializer,BS_PostResponseSerializer,BS_UpdateResponseSerializer,BS_DeleteResponseSerializer
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer

class BeneficiarySourceForUserList(APIView):
    def __init__(self):
        self.logic = LogicModule();
    
    @swagger_auto_schema(responses={200: BS_GetResponseSerializer,500 : ServerErrorResponseSerializer,404 : ErrorResponseSerializer })
    def get(self, request, format=None):
        userId = request.authUser['id']
        data, status = self.logic.beneficiarySource.getFundingSourcesForUser(userId)
        return Response(data,status=status)
    
    @swagger_auto_schema(responses={201: BS_PostResponseSerializer,500 : ServerErrorResponseSerializer,404 : ErrorResponseSerializer,409 : ErrorResponseSerializer,400 : ErrorResponseSerializer  },request_body=CreateBeneficiarySourceSerializer)
    def post(self, request, format=None):
        userId = request.authUser['id']        
        data, status = self.logic.beneficiarySource.createBeneficiarySourcesForUser(userId, request.data)
        return Response(data,status=status)    


class BeneficiarySourceForUserDetails(APIView):
    def __init__(self):
        self.logic = LogicModule();
        
    @swagger_auto_schema(responses={200: BS_DeleteResponseSerializer,400: ErrorResponseSerializer,500 : ServerErrorResponseSerializer,404 : ErrorResponseSerializer })
    def delete(self, request, beneficiarySourceId, format=None):
        userId = request.authUser['id']
        data, status = self.logic.beneficiarySource.deleteBeneficiarySourcesForUser(userId, beneficiarySourceId)
        return Response(data,status=status)
