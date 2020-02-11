from rest_framework import serializers

class IssuerRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    referenceTypeMaxChar = serializers.IntegerField()
    referenceType = serializers.CharField()
