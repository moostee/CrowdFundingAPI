from rest_framework import serializers
from DataAccessLayer.FundingGroup.model import FundingGroup
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..FundingGroupType.serializer import FundingGroupTypeSerializer
from ..User.serializer import UserSerializer

class FundingGroupSerializer(DynamicFieldsModelSerializer):
    fundingGroupType = FundingGroupTypeSerializer(many=False)
    initiator = UserSerializer(many=False, read_only=True)

    class Meta:
        model = FundingGroup
        fields = ('__all__')
