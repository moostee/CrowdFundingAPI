from rest_framework import serializers
from ..Issuer.model import Issuer
from ..DynamicSerializer import DynamicFieldsModelSerializer

class IssuerSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Issuer
        fields = ('__all__')

    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        return ret