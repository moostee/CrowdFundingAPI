from rest_framework.response import Response
from rest_framework import status
from ..Response import Response as ResponseWrapper

class ValidateUserRole:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        userRole = request.authUser['RoleName']

        if userRole == 'Admin':
            response = self.get_response(request)
            return response
        else:
            return Response(ResponseWrapper.error(message='Access Denied. You lack the permission to access this route'), status.HTTP_401_UNAUTHORIZED)
