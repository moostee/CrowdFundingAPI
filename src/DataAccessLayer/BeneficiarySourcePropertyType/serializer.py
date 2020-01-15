from rest_framework import serializers
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSourcePropertyTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroupType
        fields = ('__all__')
