from rest_framework import serializers

class FundingGroupRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    fundingGroupType = serializers.UUIDField()
    initiator = serializers.UUIDField()
    startDate = serializers.DateField()
    targetGroupDate = serializers.DateField()
    cycleDuration = serializers.CharField()
    currency = serializers.CharField()
    individualAmount = serializers.FloatField()
    targetGroupAmount = serializers.FloatField()
