from rest_framework import serializers
from DataAccessLayer.FundingTransaction.model import FundingTransaction
from ..DynamicSerializer import DynamicFieldsModelSerializer


class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingTransaction
        fields = ('__all__')
