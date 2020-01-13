from rest_framework import serializers
from ..User.model import User
from ..DynamicSerializer import DynamicFieldsModelSerializer

class IssuerSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')