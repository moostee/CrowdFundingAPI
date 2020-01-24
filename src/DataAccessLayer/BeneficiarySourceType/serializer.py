from rest_framework import serializers
from DataAccessLayer.BeneficiarySourceType.model import BeneficiarySourceType
from ..DynamicSerializer import DynamicFieldsModelSerializer
from django.utils import timezone

class BeneficiarySourceTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = BeneficiarySourceType
        fields = ('__all__')

    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        ret['updatedAt'] = timezone.localtime(timezone.now())
        return ret

