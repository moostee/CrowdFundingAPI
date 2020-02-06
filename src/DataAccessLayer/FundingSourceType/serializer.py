from rest_framework import serializers
from ..FundingSourceType.model import FundingSourceType
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..ConfigSerializer import ConfigSerializer

class FundingSourceTypeSerializer(DynamicFieldsModelSerializer):
    config = ConfigSerializer(many=True,allow_empty=False)
    class Meta:
        model = FundingSourceType
        fields = ('__all__')
    
    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        return ret


