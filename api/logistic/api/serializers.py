from rest_framework import serializers
from ..logistic_auth.models import LogisticCompany


class LogisticCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticCompany
        fields = ['id', 'passport_seria_number', 'company_name', 'address', 'country', 'description', 'company_phone',
                  'avatar']