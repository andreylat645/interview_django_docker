from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    roleId = serializers.CharField(max_length=100)
    login = serializers.CharField()
    displayName = serializers.CharField()
    pictureId = serializers.CharField()
    phoneNumber = serializers.CharField(max_length=30)
    description = serializers.CharField()
    created = serializers.CharField()

class AbonentSerializer(serializers.Serializer):
    id = serializers.CharField()
    displayName = serializers.CharField()
    description = serializers.CharField()
    pictureId = serializers.CharField()
    perimeterId = serializers.CharField()
    is_admin = serializers.CharField()
    pacsCode = serializers.CharField()
    address = serializers.CharField()
    phoneNumber = serializers.CharField()
    floor = serializers.CharField()
    room = serializers.CharField()
    cars = serializers.CharField()
    isRegistered = serializers.CharField()
    modified = serializers.CharField()