from rest_framework import serializers
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingGroupTypeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FundingGroupType
        fields = ('__all__')

        # def create(self, validated_data):
        #     return FundingGroupType(**validated_data)

        # def update(self, instance, validated_data):
        #     #when updating this model exclude the parameter createdAt from updating
        #     exclude += 'createdAt'
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.hasFixedAmount = validated_data.get('hasFixedAmount', instance.hasFixedAmount)
        #     instance.hasMaturityDate = validated_data.get('hasMaturityDate', instance.hasMaturityDate)
        #     return instance

