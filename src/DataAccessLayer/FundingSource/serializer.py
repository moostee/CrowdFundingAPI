from rest_framework import serializers
from DataAccessLayer.FundingSource.model import FundingSource
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSourceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingSource
        fields = ('__all__')
