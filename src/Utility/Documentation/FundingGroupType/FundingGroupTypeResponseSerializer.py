from rest_framework import serializers
from DataAccessLayer.FundingGroupType.serializer import FundingGroupTypeSerializer
import uuid

swaggerFieldSchema = ("id", "name")

class FundingGroupTypeGetResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingGroupTypeSerializer(many=True, fields=swaggerFieldSchema)

class FundingGroupTypeGetOneResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingGroupTypeSerializer(many=False, fields=swaggerFieldSchema)

class FundingGroupTypePostResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Funding Group type created successfully')
    responseCode = serializers.CharField(default="00")
    data = FundingGroupTypeSerializer(many=False, fields=swaggerFieldSchema)


class FundingGroupTypeUpdateResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    mesesessagees = serializers.CharField(default='Funding Group type updated successfully')
    responseCode = serializers.CharField(default="00")
    data = None

class FundingGroupTypeDeleteResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Funding Group type deleted successfully')
    responseCode = serializers.CharField(default="00")
    data = None
