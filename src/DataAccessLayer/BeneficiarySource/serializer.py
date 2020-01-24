from rest_framework import serializers
from DataAccessLayer.BeneficiarySource.model import BeneficiarySource
from ..DynamicSerializer import DynamicFieldsModelSerializer

class BeneficiarySourceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BeneficiarySource
        fields = ('__all__')
