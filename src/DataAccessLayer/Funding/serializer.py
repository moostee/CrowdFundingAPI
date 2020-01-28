from rest_framework import serializers
from ..Funding.model import Funding
from ..User.serializer import UserSerializer
from ..FundingGroup.serializer import FundingGroupSerializer
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSerializer(DynamicFieldsModelSerializer):
    beneficiary = UserSerializer(many=False, read_only=True)
    fundingGroup = FundingGroupSerializer(many=False, read_only=True)
    
    class Meta:
        model = Funding
        fields = ["id", "createdAt", "updatedAt", "isDeleted", "cycle", "amount",
                "currency", "dueDate", "status", "beneficiary", "fundingGroup"]
