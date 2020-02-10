from rest_framework import serializers
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..ConfigSerializer import ConfigSerializer
    
class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):
    config = ConfigSerializer(many=True,allow_empty=False)

    class Meta:
        model = FundingGroupType
        fields = ('__all__')

    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        return ret