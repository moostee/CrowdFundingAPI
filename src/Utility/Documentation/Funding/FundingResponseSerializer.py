import uuid
from rest_framework import serializers
from DataAccessLayer.Funding.serializer import FundingSerializer

swaggerFieldSchema = (  "id",  
                        "cycle",
                        "amount",
                        "currency",
                        "dueDate",
                        "fundingGroup",
                        "beneficiary")

class FundingGetResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='success')
    responseCode = serializers.CharField(default="00")
    data = FundingSerializer(many=True, fields=swaggerFieldSchema)

class FundingPostResponseSerializer(serializers.Serializer):

    requestId = serializers.UUIDField(default=uuid.uuid4)
    message = serializers.CharField(default='Funding Group Type created successfully')
    responseCode = serializers.CharField(default="00")
    data = FundingSerializer(many=False, fields=swaggerFieldSchema)
