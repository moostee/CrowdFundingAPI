import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from LogicLayer.FundingGroupType.service import FundingGroupTypeService as service
from DataAccessLayer.FundingGroupType.serializer import FundingGroupTypeSerializer
from Utility.Response import Response as ResponseWrapper
from Utility.Utility import Utility
from Utility.middlewares.validateUserRole import ValidateUserRole
from Utility.logger import Logger

class FundingGroupTypeList(APIView):
    def __init__(self):
        self.fundingGroupTypeService = service()
        self.logger = Logger('ControllerLayer.FundingGroupTypeList')

    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        requestId = uuid.uuid4()
        requestBody = request.data

        if 'name' in request.data: requestBody = Utility.convertFieldValueToLowerCase(request.data, 'name')
        validData = FundingGroupTypeSerializer(data=requestBody)

        if(validData.is_valid() is False):
            self.logger.Info(r"Create Funding Group Type. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), requestId))
            return Response(ResponseWrapper.error(requestId, error=validData.errors, responseCode='01'))
        return Response(self.fundingGroupTypeService.createFundingGroupType(validData.data))

    def get(self,request,format=None):
        return Response(self.fundingGroupTypeService.getAllFundingGroupType())

class FundingGroupTypeDetail(APIView):
    def __init__(self):
        self.fundingGroupTypeService = service()
        self.logger = Logger('ControllerLayer.FundingGroupTypeDetail')

    def get(self, request, pk, format=None):
        return Response(self.fundingGroupTypeService.getOneFundingGroupType(pk))

    @method_decorator(ValidateUserRole)
    def put(self, request, pk, format=None):
        return Response(self.fundingGroupTypeService.updateFundingGroupType(pk, request.data))
    
    @method_decorator(ValidateUserRole)
    def delete(self, request, pk, format=None):
        return Response(self.fundingGroupTypeService.deleteFundingGroupType(pk))
    