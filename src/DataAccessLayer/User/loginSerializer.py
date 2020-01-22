from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=100, required=False)
    pin = serializers.CharField(max_length=6, required=False)
    Password = serializers.CharField(max_length=100, required=False)
