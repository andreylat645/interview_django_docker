from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    roleId = serializers.CharField(max_length=100)
    login = serializers.CharField()
    displayName = serializers.CharField()
    pictureId = serializers.CharField()
    phoneNumber = serializers.CharField(max_length=30)
    description = serializers.CharField()
    created = serializers.CharField()
