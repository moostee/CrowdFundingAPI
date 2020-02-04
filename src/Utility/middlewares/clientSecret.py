from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from Utility.Response import Response as ResponseWrapper
from Utility.Utility import Utility
import uuid
from Utility.logger import Logger


class ClientSecret:   

    def __init__(self, get_response):
        self.get_response = get_response
        Response.accepted_renderer = JSONRenderer()
        Response.accepted_media_type = "application/json"
        Response.renderer_context = {}
        self.logger = Logger('Middleware.ClientSecret')
        self.pathsToExempt = ['swagger', 'redoc', 'api']

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        requestId = uuid.uuid4()
        clientSecret = request.headers.get('client-secret')
        if Utility.checkExemptPaths(request.path, self.pathsToExempt):
            return None

        if not clientSecret:
            self.logger.Info(r"Invalid Access. Attempt to access {} without client-secret in header. n\ REQUESTID => {}".format(request.path, requestId))
            return Response(ResponseWrapper.error(requestId, message='Unauthorized access. Missing client token.', responseCode='02'), status.HTTP_401_UNAUTHORIZED)

