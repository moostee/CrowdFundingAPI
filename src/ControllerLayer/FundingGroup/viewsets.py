from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.FundingGroup.service import FundingGroupService
from Utility.middlewares.validateUserRole import ValidateUserRole
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from Utility.Documentation.FundingGroup.ResponseSerializer import PostFundingGroupResponseSerializer, GetFundingGroupResponseSerializer
from DataAccessLayer.FundingGroup.serializer import FundingGroupSerializer

class FundingGroup(APIView):
    def __init__(self):
        self.Role = FundingGroupService()

    @swagger_auto_schema(responses={201: PostFundingGroupResponseSerializer,404:"Funding group cannot be created at this time. Please contact the administrator.", 400 : "Error occured validating your request. {Appropriate Error}",409 : "Please try again. Something unexpected happend.",500: "An error occured while processing your request. Please try again later"},request_body=FundingGroupSerializer())
    def post(self, request, format=None):
        response,status = self.Role.createFundinGroup(request.data,user=request.authUser)
        return Response(response, status=status)

    @method_decorator(ValidateUserRole)
    @swagger_auto_schema(responses={200: GetFundingGroupResponseSerializer,500 : "An error occured while processing your request. Please try again later"})
    def get(self, request, format=None):
        return Response(self.Role.getFundingGroups())
