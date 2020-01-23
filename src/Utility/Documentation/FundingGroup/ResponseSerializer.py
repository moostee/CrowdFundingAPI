from rest_framework import serializers
from DataAccessLayer.FundingGroup.serializer import FundingGroupSerializer
import uuid

class GetFundingGroupResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingGroupSerializer(many=True)

class PostFundingGroupResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type created successfully')
    responseCode = serializers.CharField(default="00")
    data = FundingGroupSerializer(many=False)
