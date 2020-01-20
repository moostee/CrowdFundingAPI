from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.LogicModule import LogicModule

class FundingSourceForUser(APIView):
    def __init__(self):
        self.logic = LogicModule();
    
    def get(self, request, userId, format=None):
        return Response(self.logic.fundingSourceService.getFundingSourcesForUser(userId))
