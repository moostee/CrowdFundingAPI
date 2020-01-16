from rest_framework.views import APIView
from rest_framework.response import Response
from LogicLayer.Role.service import RoleService
from django.utils.decorators import method_decorator
from Utility.middlewares.validateUserRole import ValidateUserRole

class RoleList(APIView):
    def __init__(self):
        self.Role= RoleService()

    @method_decorator(ValidateUserRole)
    def post(self, request, format=None):
        return Response(self.Role.createRole(request.data))

    def get(self, request, format=None):
        return Response(self.Role.getAllRoles())

class RoleDetails(APIView):
    def __init__(self):
        self.Role = RoleService()
    
    def get(self, request, pk, format=None):
        return Response(self.Role.getOneRole(pk))

    @method_decorator(ValidateUserRole)
    def put(self, request, pk, format=None):
        return Response(self.Role.updateRole(request.data, pk))

    @method_decorator(ValidateUserRole)
    def delete(self, request, pk, format=None):
        return Response(self.Role.deleteRole(pk))
