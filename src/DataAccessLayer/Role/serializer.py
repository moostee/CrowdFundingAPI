from rest_framework import serializers
from DataAccessLayer.Role.model import Role
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Role
        fields = ('__all__')
