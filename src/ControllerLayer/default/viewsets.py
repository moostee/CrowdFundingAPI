from rest_framework.views import APIView
from rest_framework.response import Response
from Utility.Response import Response as response
from drf_yasg.utils import swagger_auto_schema
from Utility.logger import Logger
import uuid

class DefaultViewSet(APIView):
    @swagger_auto_schema(operation_description="API Welcome View", responses={200: '{"Message":"Welcome crowdfunding api"}'})
    def get(self, request, format=None):
        logger = Logger('ControllerLayer.Default')
        requestId = uuid.uuid4()
        logger.Info(r"Default Route was called. \n REQUESTID => {}".format(requestId))
        return Response(response.success(requestId, data={"Message":"Welcome crowdfunding api"}))
