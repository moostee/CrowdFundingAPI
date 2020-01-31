from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.User.service import UserService as service
from DataAccessLayer.User.serializer import UserSerializer
from Utility.Response import Response as ResponseWrapper
from Utility.Requests import Request
from Utility.logger import Logger
import uuid


class UserSignup(APIView):
    def __init__(self):
        self.UserService = service()

    def post(self, request, format=None):
        client_secret = request.META.get('HTTP_CLIENT_SECRET')
        response,status = self.UserService.createUser(request.data, client_secret)
        return Response(response, status=status)


class UserLogin(APIView):

    def __init__(self):
        self.userService = service()
        self.logger = Logger('ControllerLayer.UserLogin')

    def post(self, request, format=None):
        client_secret = request.META.get('HTTP_CLIENT_SECRET')
        response,status = self.userService.verifyUser(request.data, client_secret)
        return Response(response, status=status)
