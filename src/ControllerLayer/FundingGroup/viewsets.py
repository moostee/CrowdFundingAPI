from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.FundingGroup.service import FundingGroupService
from Utility.middlewares.validateUserRole import ValidateUserRole
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.FundingGroup.ResponseSerializer import PostFundingGroupResponseSerializer, GetFundingGroupResponseSerializer
from Utility.Documentation.FundingGroup.RequestSerializer import FundingGroupRequestSerializer
from Utility.Documentation.ErrorResponseSerializer import ErrorResponseSerializer
from Utility.Documentation.ServerErrorResponseSerializer import ServerErrorResponseSerializer

from DataAccessLayer.FundingGroup.serializer import FundingGroupSerializer

class FundingGroup(APIView):
    def __init__(self):
        self.fundingGroup = FundingGroupService()

    @swagger_auto_schema(responses={201: PostFundingGroupResponseSerializer,400 : ErrorResponseSerializer,401 : ErrorResponseSerializer,409 : ErrorResponseSerializer,500:ServerErrorResponseSerializer},request_body=FundingGroupRequestSerializer())
    def post(self, request, format=None):
        response,status = self.fundingGroup.createFundinGroup(request.data,user=request.authUser)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: GetFundingGroupResponseSerializer,500 : ServerErrorResponseSerializer})
    def get(self, request, format=None):
        response,status = self.fundingGroup.getFundingGroups()
        return Response(response,status=status)
