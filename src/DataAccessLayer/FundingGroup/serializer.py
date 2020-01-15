from rest_framework import serializers
from DataAccessLayer.FundingGroup.model import FundingGroup
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroup
        fields = ('__all__')
