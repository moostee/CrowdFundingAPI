from rest_framework import serializers
from DataAccessLayer.BeneficiarySource.model import BeneficiarySource
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..Issuer.serializer import IssuerSerializer
from ..BeneficiarySourceType.serializer import BeneficiarySourceTypeSerializer
from ..BeneficiarySourceProperty.serializer import BeneficiarySourcePropertySerializer
import uuid
class BeneficiarySourceSerializer(DynamicFieldsModelSerializer):

    beneficiarySourceType = BeneficiarySourceTypeSerializer(many=False)
    issuer = IssuerSerializer(many=False)

    class Meta:
        model = BeneficiarySource
        fields = ('__all__')


class DeleteBeneficiarySourceSerializer(serializers.Serializer):
    beneficiaryId = serializers.UUIDField()

class BeneficiaryPropertyValueSerializer(serializers.Serializer):
    propertyType = serializers.CharField(max_length=100,allow_blank=False)
    propertyValue = serializers.CharField(max_length=100,allow_blank=False)

class CreateBeneficiarySourceSerializer(serializers.Serializer):
    beneficiarySourceTypeId = serializers.UUIDField(required=True)
    destinationNumber = serializers.CharField(max_length=100,allow_blank=False)
    issuerId = serializers.UUIDField(required=True)
    property = BeneficiaryPropertyValueSerializer(many=True,allow_empty=False)


