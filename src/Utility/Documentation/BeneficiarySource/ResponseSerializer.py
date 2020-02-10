from rest_framework import serializers
from DataAccessLayer.BeneficiarySource.serializer import BeneficiarySourceSerializer
import uuid




class BS_GetResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceSerializer(many=True)

class BS_PostResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source created successfully')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceSerializer(many=False)


class BS_UpdateResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    mesesessagees = serializers.CharField(default='Beneficiary source updated successfully')
    responseCode = serializers.CharField(default="00")
    data = BeneficiarySourceSerializer(many=False)

class BS_DeleteResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Beneficiary source type deleted successfully')
    responseCode = serializers.CharField(default="00")
    data = None




