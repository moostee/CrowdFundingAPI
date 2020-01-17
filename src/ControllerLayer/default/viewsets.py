from rest_framework.views import APIView
from rest_framework.response import Response
from Utility.Response import Response as response

class DefaultViewSet(APIView):
    def get(self, request, format=None):
        return Response(response.success(data={"Message":"Welcome crowdfunding api"}))
