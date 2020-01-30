from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    pin = serializers.CharField(required=False)
