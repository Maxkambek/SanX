from rest_framework import serializers
from api.client.client_auth.models import ClientFullName, ClientDateBirth, ClientAvatar
from api.client.client_main.models import Order, OrderFiles, ReplyDriver, ClientWishList, DriverClientOrderContract
from api.common.v1.serializers import CountrySerializer2
from api.driver.driver_auth.serializers import DriverInformationSerializer, DriverInfoFullSerializer
from api.common.accounts.models import Account


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


class OrderFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFiles
        fields = ['id', 'file']


class ClientProfileSerializer(serializers.ModelSerializer):
    client_full_name = ClientFullNameSerializer(many=False)
    client_avatar = ClientAvatarSerializer(many=False)
    client_birth = ClientDateBirthSerializer(many=False)

    class Meta:
        model = Account
        fields = ['id', 'phone', 'bio', 'client_full_name', 'client_avatar', 'client_birth']


class ClientProfileChangeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=123)
    last_name = serializers.CharField(max_length=123)
    surname = serializers.CharField(max_length=123)
    date_birth = serializers.DateField()
    avatar = serializers.FileField(allow_empty_file=True)

    class Meta:
        model = Account
        fields = ['phone', 'bio', 'name', 'last_name', 'surname', 'date_birth', 'avatar']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'file_1', 'file_2', 'file_3', 'file_4', 'file_5', 'file_6', 'transport_type', 'name', 'location_from',
            'location_to',
            'date', 'weight', 'volume_m3', 'price', 'type_payment', 'description',
            'created_at', 'updated_at', 'status', 'views', 'longitude', 'latitude'
        ]


class OrderListSerializer(serializers.ModelSerializer):
    location_from = CountrySerializer2(many=False)
    location_to = CountrySerializer2(many=False)

    class Meta:
        model = Order
        fields = [
            'id', 'file_1', 'file_2', 'file_3', 'file_4', 'file_5', 'file_6', 'transport_type', 'name', 'location_from',
            'location_to',
            'date', 'weight', 'volume_m3', 'price', 'type_payment', 'description',
            'created_at', 'updated_at', 'status', 'views', 'longitude', 'latitude'
        ]


class MyOrdersOtClicksSerializer(serializers.ModelSerializer):
    owner = DriverInformationSerializer(read_only=True)

    class Meta:
        model = ReplyDriver
        fields = ['id', 'order', 'created_at', 'owner']


class OrderDetailSerializer(serializers.ModelSerializer):
    order_clicks = MyOrdersOtClicksSerializer(many=True)
    location_from = CountrySerializer2(many=False)
    location_to = CountrySerializer2(many=False)

    class Meta:
        model = Order
        fields = ['id', 'transport_type', 'name', 'location_from', 'location_to',
                  'date', 'weight', 'price', 'type_payment', 'description', 'file_1', 'file_2', 'file_3', 'file_4',
                  'file_5', 'file_6',
                  'created_at', 'updated_at', 'status', 'order_clicks']


class ReplyDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyDriver
        fields = ['id', 'order', 'created_at']


class MyClicksSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = ReplyDriver
        fields = ['id', 'order', 'created_at']


class GiveWorkSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['worker_id', 'order_id']


class ClientWishListSerializer(serializers.ModelSerializer):
    driver = DriverInfoFullSerializer(read_only=True)

    class Meta:
        model = ClientWishList
        fields = ['id', 'driver']


class ClientWishListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWishList
        fields = ['driver']


class DriverClientContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverClientOrderContract
        fields = ['id', 'order_id', 'sender', 'default_price', 'receiver', 'updated_price', 'created_at', 'status']


class DriverClientContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverClientOrderContract
        fields = ['order_id', 'updated_price', 'receiver']
