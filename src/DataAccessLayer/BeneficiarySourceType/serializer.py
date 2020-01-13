from rest_framework import serializers
from ..FundingSourceType.model import FundingSourceType
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSourceTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingSourceType
        fields = ('__all__')