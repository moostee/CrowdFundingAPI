from rest_framework.response import Response
from ..jwt import Jwt
from rest_framework.renderers import JSONRenderer
from Utility.Response import Response as ResponseWrapper
from Utility.Utility import Utility
import uuid
from Utility.logger import Logger
import os

jwt_secret = os.environ.get('JWT_SECRET')

class Authentication:   

    def __init__(self, get_response):
        self.get_response = get_response
        Response.accepted_renderer = JSONRenderer()
        Response.accepted_media_type = "application/json"
        Response.renderer_context = {}
        self.logger = Logger('Middleware.Authentication')
        self.pathsToExempt = ['admin', 'swagger', 'redoc', 'api', 'signup', 'signin']

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        requestId = uuid.uuid4()
        if Utility.checkExemptPaths(request.path, self.pathsToExempt):
            return None
        token = request.headers.get('Authorization')

        if not token:
            self.logger.Info(r"Unauthorized Access. Attempt to access {} without token in header. n\ REQUESTID => {}".format(request.path, requestId))
            return Response(ResponseWrapper.error(requestId, message='Unauthorized. No token in header', responseCode='02'), status=401)
        else:
            try:
                tokenString = token.split(' ')[1]
                decodedUserObj = Jwt.DecodeJWT(tokenString, jwt_secret)
                request.authUser = decodedUserObj
                return None
            except BaseException as ex:
                self.logger.Info(r"Unauthorized Access. Invalid Token in accessing {} with error {} n\ REQUESTID => {}".format(request.path,str(ex),requestId))
                return Response(ResponseWrapper.error(requestId, message='Invalid Token', responseCode='02'), 401)
