from rest_framework import serializers
from DataAccessLayer.FundingGroup.model import FundingGroup
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..FundingGroupType.serializer import FundingGroupTypeSerializer
from ..User.serializer import UserSerializer
from Utility.Validator import Validator
from datetime import date

class FundingGroupPostSerializer(DynamicFieldsModelSerializer):
    def __getRequiredFundingGroupConfiguration(self,fundingGroupType,data):
        config = []
        startDate = { "field": "startDate", "rules": [{"key":"required", "value":True}, {"key":"type","value":"date"}, {"key":"minValue","value":date.today()} ] }
        config.append(startDate)
    
        if fundingGroupType.hasFixedIndividualAmount:
            individualAmount = { "field": "individualAmount", "rules": [{"key":"required", "value":True}, {"key":"type","value":"number"} ] }
            config.append(individualAmount)

        if fundingGroupType.hasFixedGroupAmount:
            targetGroupAmount = { "field": "targetGroupAmount", "rules": [{"key":"required", "value":True}, {"key":"type","value":"number"} ] }
            config.append(targetGroupAmount)
        
        if fundingGroupType.hasMaturityDate:
            targetGroupDate = { "field": "targetGroupDate", "rules": [{"key":"required", "value":True}, {"key":"type","value":"date"}, {"key":"minValue","value":data['startDate']} ] }
            config.append(targetGroupDate)
        
        if not fundingGroupType.hasFixedDefaultCycle and not fundingGroupType.defaultCycleDuration:
            cycleDuration = { "field": "cycleDuration", "rules": [{"key":"required", "value":True}, {"key":"regex","value":"\d+(d|w|m)"} ] }
            config.append(cycleDuration)
        return config
    
    def validate(self, data):
        config = self.__getRequiredFundingGroupConfiguration(data['fundingGroupType'],data)
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
