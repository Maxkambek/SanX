from rest_framework import serializers
from api.common.accounts.models import Account, VerifyCode
from api.common.main.models import Country, Location, FAQ, News, Banners, ChatMessage, VersionProject


class VersionProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionProject
        fields = '__all__'


class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['get_user_info']


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ['id', 'title', 'description', 'file']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'flag_img', 'code']


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


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'file', 'title', 'content', 'sub_content', 'created_at']
