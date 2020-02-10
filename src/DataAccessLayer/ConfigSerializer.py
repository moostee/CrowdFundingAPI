from rest_framework import serializers


class AnyField(serializers.Field):
    def to_internal_value(self, data):
        return data
    
    def to_representation(self, data):
        return data

class RulesSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=50,allow_blank=False)
    value = AnyField(allow_null=False)

class ConfigSerializer(serializers.Serializer):
    field = serializers.CharField(max_length=50,allow_blank=False)
    label = serializers.CharField(max_length=50,allow_blank=False)
    type = serializers.CharField(max_length=50,allow_blank=False)
    tip = serializers.CharField(max_length=50,allow_blank=False)
    rules = RulesSerializer(many=True,allow_empty=False)

