from rest_framework import serializers
from DataAccessLayer.FundingGroupUser.model import FundingGroupUser
from ..DynamicSerializer import DynamicFieldsModelSerializer


class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroupUser
        fields = ('__all__')
