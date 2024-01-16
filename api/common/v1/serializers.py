from rest_framework import serializers
from api.common.accounts.models import Account, VerifyCode
from api.common.main.models import Country, Location


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'flag_img']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class VerifyCodeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=30)

    class Meta:
        model = VerifyCode
        fields = ['phone', 'code', 'role']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class LoginVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = ['phone', 'code']
