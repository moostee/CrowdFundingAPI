from rest_framework import serializers
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
import uuid

class GetResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceTypeSerializer(many=True,fields=('id','name'))

class PostResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type created successfully')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceTypeSerializer(many=False,fields=('id','name'))

class UpdateResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type updated successfully')
    responseCode = serializers.CharField(default="00")
    data = None

class DeleteResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type deleted successfully')
    responseCode = serializers.CharField(default="00")
    data = None
