from rest_framework import serializers
import uuid

class ServerErrorResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Error occured while processing your request')
    responseCode = serializers.CharField(default="99")
    error = None