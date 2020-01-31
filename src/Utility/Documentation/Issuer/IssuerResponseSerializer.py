from rest_framework import serializers
from DataAccessLayer.Issuer.serializer import IssuerSerializer
import uuid

class GetIssuerResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = IssuerSerializer(many=True)

class GetOneIssuerResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = IssuerSerializer(many=False)

class PostIssuerResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Issuer successfully created.')
    responseCode = serializers.CharField(default="00")
    data = IssuerSerializer(many=False)


class UpdateIssuerResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    mesesessagees = serializers.CharField(default='Issuer successfully updated')
    responseCode = serializers.CharField(default="00")
    data = IssuerSerializer(many=False)

class DeleteIssuerResponseSerializer(serializers.Serializer):
    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Issuer was successfully deleted')
    responseCode = serializers.CharField(default="00")
    data = None
