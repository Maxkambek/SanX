from rest_framework import serializers
from api.client.client_auth.models import ClientFullName, ClientDateBirth, ClientAvatar


class ClientFullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFullName
        fields = ['name', 'last_name', 'surname']


class ClientDateBirthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDateBirth
        fields = ['birth_date']


class ClientAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAvatar
        fields = ['image']
