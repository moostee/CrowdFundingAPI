from rest_framework import serializers
from DataAccessLayer.FundingGroup.model import FundingGroup
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingGroupSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroup
        fields = ('__all__')
