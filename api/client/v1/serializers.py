from rest_framework import serializers
from api.client.client_auth.models import ClientFullName, ClientDateBirth, ClientAvatar
from api.client.client_main.models import Order, OrderFiles, ReplyDriver, ClientWishList
from api.driver.driver_auth.serializers import DriverInformationSerializer, DriverInfoFullSerializer


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


class OrderSerializer(serializers.ModelSerializer):
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
