from rest_framework import serializers
from DataAccessLayer.BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
import uuid

class BST_GetResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceTypeSerializer(many=True)

class BST_PostResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type created successfully')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceTypeSerializer(many=False)


class BST_UpdateResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    mesesessagees = serializers.CharField(default='Beneficiary source type updated successfully')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceTypeSerializer(many=False)

class BST_DeleteResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type deleted successfully')
    responseCode = serializers.CharField(default="00")
    data = None

