import uuid
from rest_framework.response import Response
from rest_framework import status
from ..Response import Response as ResponseWrapper
import uuid
from Utility.logger import Logger

class ValidateUserRole:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = Logger('Utility.Authentication')

    def __call__(self, request, pk=None):
        requestId = uuid.uuid4()
        userRole = request.authUser['roleName']

        if userRole == 'Admin':
            if request.method == 'POST':
                response = self.get_response(request)
            else:
                response = self.get_response(request, pk)
            return response
        else:
            self.logger.Info(r"Unauthorized Access. User {} attempting to access {} without admin rights. n\ REQUESTID => {}".format(request.authUser['id'], request.path, requestId))
            return Response(ResponseWrapper.error(requestId, message='Access Denied. You lack the permission to access this route', responseCode='02'), status.HTTP_401_UNAUTHORIZED)
