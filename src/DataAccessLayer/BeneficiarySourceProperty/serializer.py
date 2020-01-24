from rest_framework import serializers
from DataAccessLayer.BeneficiarySourceProperty.model import BeneficiarySourceProperty
from ..DynamicSerializer import DynamicFieldsModelSerializer

class BeneficiarySourcePropertySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BeneficiarySourceProperty
        fields = ('__all__')
