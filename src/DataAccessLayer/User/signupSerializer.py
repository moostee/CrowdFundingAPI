from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(max_length=14)
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    email = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    pin = serializers.CharField(required=False)
