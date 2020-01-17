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
        self.logger = Logger('ControllerLayer.UserSignup')
        self.UserService = service()

    def post(self, request, format=None):
        requestId = uuid.uuid4()
        validData = UserSerializer(data=request.data)
        client_secret = request.META.get('HTTP_CLIENT_SECRET')
        if(not validData.is_valid()):
            self.logger.Info(r"User signup. Failed validation with: {}, n\ REQUESTID => {}".format(str(validData.errors), requestId))
            return Response(ResponseWrapper.error(requestId, message="Validation error occured processing request", error=validData.errors, responseCode='01'))
        return Response(self.UserService.createUser(validData.data, client_secret))
