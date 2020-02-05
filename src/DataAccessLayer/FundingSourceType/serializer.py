from rest_framework import serializers
from ..FundingSourceType.model import FundingSourceType
from ..DynamicSerializer import DynamicFieldsModelSerializer

class ConfigSerializer(serializers.Serializer):
    field = serializers.CharField(max_length=50,allow_blank=False)
    label = serializers.CharField(max_length=50,allow_blank=False)
    type = serializers.CharField(max_length=50,allow_blank=False)
    tip = serializers.CharField(max_length=50,allow_blank=False)
    rules = serializers.DictField(allow_empty=False)

class FundingSourceTypeSerializer(DynamicFieldsModelSerializer):
    config = ConfigSerializer(many=True,allow_empty=False)
    class Meta:
        model = FundingSourceType
        fields = ('__all__')
    
    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        return ret


