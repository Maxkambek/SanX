from rest_framework import serializers
from .models import *


class DriverFullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverFullName
        fields = ['name', 'last_name', 'surname']


class DriverDateBirthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDateBirth
        fields = ['date']


class DriverDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDirection
        fields = ['direction_from', 'direction_to']


class DriverAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAvatar
        fields = ['image']


class DriverPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPassport
        fields = ['seria_num', 'front_side', 'with_residence', 'face_img']


class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ['license_seria_num', 'license_expiration_date', 'front_side', 'back_side', 'face_img']


class DriverCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCompany
        fields = ['company_name']


class DriverPaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPaymentType
        fields = ['payment_type']


class DriverTransportDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverTransportDetails
        fields = ['transport_type', 'model_transport', 'color_transport',
                  'transport_made_date', 'tons_from', 'tons_to', 'volume3_from', 'volume3_to']


class TechnicalPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalPassport
        fields = ['country', 'serial_number', 'front_side_img', 'back_side_img']


class TransportImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportImages
        fields = ['transport_front', 'transport_left', 'transport_behind', 'transport_right', 'row_seats', 'baggage']


class TransportWeightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportWeightType
        fields = ['id', 'name', 'description']


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = ['id', 'name', 'image']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerType
        fields = ['id', 'name']


class ModelTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTransport
        fields = ['id', 'name', 'description']


class ColorTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorTransport
        fields = ['id', 'name', 'color']


class DriverInformationSerializer(serializers.ModelSerializer):
    driver_full_name = DriverFullNameSerializer(read_only=True, many=False)
    driver_avatar = DriverAvatarSerializer(read_only=True, many=False)

    class Meta:
        model = Account
        fields = ['driver_full_name', 'driver_avatar']


class DriverInfoFullSerializer(serializers.ModelSerializer):
    driver_full_name = DriverFullNameSerializer(read_only=True, many=False)
    driver_avatar = DriverAvatarSerializer(read_only=True, many=False)
    driver_direction = DriverDirectionSerializer(read_only=True, many=False)
    driver_company = DriverCompanySerializer(read_only=True, many=False)
    driver_payment_type = DriverPaymentTypeSerializer(read_only=True, many=False)
    driver_transport_images = TransportImagesSerializer(read_only=True, many=True)

    class Meta:
        model = Account
        fields = ['driver_full_name', 'driver_avatar', 'driver_direction', 'driver_company', 'driver_payment_type',
                  'driver_transport_images']
