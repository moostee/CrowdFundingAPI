from rest_framework import serializers
from DataAccessLayer.FundingGroup.model import FundingGroup
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..FundingGroupType.serializer import FundingGroupTypeSerializer
from ..User.serializer import UserSerializer
from Utility.Validator import Validator
from datetime import date

class FundingGroupPostSerializer(DynamicFieldsModelSerializer):
    def validate(self, data):
        config = data['fundingGroupType'].config
        validateConfig = Validator(data,config).validate()
        if not validateConfig.isValid:
            raise serializers.ValidationError(detail=validateConfig.errors)
        return self

    class Meta:
        model = FundingGroup
        fields = ('__all__')
        extra_kwargs = {
            "code": {'required': False},
            "initiator": {"required": False},
        }
        validators = []
