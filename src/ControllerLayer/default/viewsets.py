from rest_framework.views import APIView
from rest_framework.response import Response
from Utility.Response import Response as response
from drf_yasg.utils import swagger_auto_schema

class DefaultViewSet(APIView):
    @swagger_auto_schema(operation_description="API Welcome View", responses={200: '{"Message":"Welcome crowdfunding api"}'})
    def get(self, request, format=None):
        return Response(response.success(data={"Message":"Welcome crowdfunding api"}))
