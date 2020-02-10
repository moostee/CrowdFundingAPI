from rest_framework import serializers
import uuid

class ErrorResponseSerializer(serializers.Serializer):
    
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default="""{{appropriateError}}""")
    responseCode = serializers.CharField(default="03")
    data = None