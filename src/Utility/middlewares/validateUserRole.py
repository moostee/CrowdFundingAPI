from rest_framework.response import Response
from rest_framework import status
from ..Response import Response as ResponseWrapper
import uuid

class ValidateUserRole:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        requestId = uuid.uuid4()
        userRole = request.authUser['roleName']

        if userRole == 'Admin':
            response = self.get_response(request)
            return response
        else:
            return Response(ResponseWrapper.error(requestId, message='Access Denied. You lack the permission to access this route'), status.HTTP_401_UNAUTHORIZED)
