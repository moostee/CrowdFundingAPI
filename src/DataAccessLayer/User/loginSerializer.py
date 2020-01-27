from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(max_length=14)
