from rest_framework import serializers
from ..User.loginModel import LoginModel
from ..DynamicSerializer import DynamicFieldsModelSerializer


class LoginSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = LoginModel
        fields = ('__all__')
