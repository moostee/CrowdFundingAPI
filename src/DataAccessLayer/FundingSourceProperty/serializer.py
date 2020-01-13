from rest_framework import serializers
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSourcePropertySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroupType
        fields = ('__all__')
