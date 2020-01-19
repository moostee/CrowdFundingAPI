from rest_framework import serializers
from DataAccessLayer.FundingSourceType.serializer import FundingSourceTypeSerializer
import uuid

swaggerFieldSchema = ("id", "name")

class FundingSourceTypeGetResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingSourceTypeSerializer(many=True, fields=swaggerFieldSchema)

class FundingSourceTypeGetOneResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingSourceTypeSerializer(many=False, fields=swaggerFieldSchema)

class FundingSourceTypePostResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Funding source type created successfully')
    responseCode = serializers.CharField(default="00")
    data = FundingSourceTypeSerializer(many=False, fields=swaggerFieldSchema)


class FundingSourceTypeUpdateResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    mesesessagees = serializers.CharField(default='Funding source type updated successfully')
    responseCode = serializers.CharField(default="00")
    data = None

class FundingSourceTypeDeleteResponse(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Funding source type deleted successfully')
    responseCode = serializers.CharField(default="00")
    data = None
