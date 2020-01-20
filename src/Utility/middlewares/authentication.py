import environ
import json
from rest_framework.response import Response
from ..jwt import Jwt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from ..Response import Response as ResponseWrapper
from Utility.Utility import Utility

env = environ.Env()
environ.Env.read_env()

class Authentication:
    def __init__(self, get_response):
        self.get_response = get_response
        Response.accepted_renderer = JSONRenderer()
        Response.accepted_media_type = "application/json"
        Response.renderer_context = {}
        self.pathsToExempt = ['admin', 'swagger', 'redoc', 'api', 'signup', 'login']

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if Utility.checkExemptPaths(request.path, self.pathsToExempt):
            return None
        token = request.headers.get('Authorization')
        if not token:
            return Response(ResponseWrapper.error(message='Unauthorized. No token in header'), status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                tokenString = token.split(' ')[1]
                decodedUserObj = Jwt.DecodeJWT(tokenString, env('SECRET'))
                request.authUser = json.loads(decodedUserObj['actort'])
                return None
            except:
                return Response(ResponseWrapper.error(message='Invalid Token'), status.HTTP_401_UNAUTHORIZED)
    