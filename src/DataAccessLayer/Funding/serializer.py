from rest_framework import serializers
from ..Funding.model import Funding
from ..DynamicSerializer import DynamicFieldsModelSerializer

class FundingSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Funding
        fields = ('__all__')