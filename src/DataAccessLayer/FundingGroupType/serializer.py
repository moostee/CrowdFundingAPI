from rest_framework import serializers
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from ..DynamicSerializer import DynamicFieldsModelSerializer
from ..ConfigSerializer import ConfigSerializer
import re
    
class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):
    config = ConfigSerializer(many=True,allow_empty=False)

    def checkStartDateValue(self,config):
        hasError = False
        errorMessage = ''
        startDate = next(item for item in config if item["field"] == "startDate")
        startDateMinDate =  next(rule for rule in startDate['rules'] if rule['key'] == 'minDate')
        datePattern = "\d+(d|w|m)"
        if not isinstance(startDateMinDate['value'], str) : 
            hasError = True
            errorMessage = "start date configuration rule key [minDate] accepts value of type string"
            return hasError, errorMessage

        if not re.match(datePattern, startDateMinDate['value']):
            hasError = True
            errorMessage = "Start date configuration rule with key [minDate] accepts value of these formats [0d,1d,2d,1w,2w,1m,2m] d- days, w-weeks, m-months"

        return hasError, errorMessage

    def checkRegexValue(self,config):
        hasError = False
        errorMessage = ''
        cycleDuration = next(item for item in config if item["field"] == "cycleDuration")
        cycleDurationRegex =  next(rule for rule in cycleDuration['rules'] if rule['key'] == 'regex')
        
        if not isinstance(cycleDurationRegex['value'], str) : 
            hasError = True
            errorMessage = "cycle duration configuration rule key [regex] accepts value of type string"
        return hasError, errorMessage



    def ValidateFieldBasedOnDataValue(self,data):
        config = data.pop('config')
        configurationsFieldName = [field['field'] for field in config]
        errors = {}
        errorMessage = 'This field name needs to be defined in the configuration rules'
        ruleError = 'This configuration requires "key" : "{}" and "value" as part of the rules'

        if 'name' not in configurationsFieldName:
            errors['name'] = [errorMessage]

        if 'name' not in configurationsFieldName:
            errors['description'] = [errorMessage]

        if 'startDate' not in configurationsFieldName:
            errors['startDate'] = [errorMessage]
        elif 'minDate' not in [field['key'] for field in (next(item for item in config if item["field"] == "startDate")['rules'])]: 
            errors['startDate'] = [ruleError.format('minDate')]
        else: 
            hasError, dateErrorMessage = self.checkStartDateValue(config)
            if hasError : errors['startDate'] = [dateErrorMessage]  
    
        if data['hasFixedIndividualAmount']:
            if 'individualAmount' not in configurationsFieldName :
                errors['individualAmount'] = [errorMessage]

        if data['hasFixedGroupAmount']:
            if 'targetGroupAmount' not in configurationsFieldName :
                errors['targetGroupAmount'] = [errorMessage]  

        if data['hasMaturityDate']:
            if 'targetGroupDate' not in configurationsFieldName :
                errors['targetGroupDate'] = [errorMessage] 
        
        if data['hasFixedDefaultCycle'] and not data['defaultCycleDuration']:
            if 'cycleDuration' not in configurationsFieldName :
                errors['cycleDuration'] = [errorMessage] 
            elif 'regex' not in [field['key'] for field in (next(item for item in config if item["field"] == "cycleDuration")['rules'])]: 
                errors['cycleDuration'] = [ruleError.format('regex')]
            else :
                hasError, cycleDurationErrorMessage = self.checkRegexValue(config)
                if hasError : errors['cycleDuration'] = [cycleDurationErrorMessage]

        return errors

    class Meta:
        model = FundingGroupType
        fields = ('__all__')

    def validate(self, data):

        errors = self.ValidateFieldBasedOnDataValue(data)
        if not re.match('\d+(d|w|m)', data['defaultCycleDuration']) :
            errors['defaultCycleDuration'] = ['This field requires value in these format[1d,2d,1w,2w,1m,2m] d- days, w-weeks, m-months'] 
    
        if errors is not None:
            raise serializers.ValidationError(detail=errors)

        return self

    def to_internal_value(self, instance):
        ret = super().to_internal_value(instance)
        ret['name'] = ret['name'].lower()
        return ret