from rest_framework import serializers
from ..Issuer.model import Issuer
from ..DynamicSerializer import DynamicFieldsModelSerializer

class IssuerSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Issuer
        fields = ('__all__')