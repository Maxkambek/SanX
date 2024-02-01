from rest_framework import serializers
from api.client.client_auth.models import ClientFullName, ClientDateBirth, ClientAvatar
from api.client.client_main.models import Order, OrderFiles, ReplyDriver
from api.driver.driver_auth.serializers import DriverInformationSerializer


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
    order_files = OrderFilesSerializer(many=True)

    def create(self, validated_data):
        files_data = validated_data.pop('order_files')
        order = Order.objects.create(**validated_data)
        for file in files_data:
            OrderFiles.objects.create(order=order, file=file)
        return order

    class Meta:
        model = Order
        fields = [
            'id', 'transport_type', 'name', 'location_from', 'location_to',
            'date', 'weight', 'volume_m3', 'price', 'type_payment', 'description',
            'created_at', 'updated_at', 'status', 'order_files'
        ]


class MyOrdersOtClicksSerializer(serializers.ModelSerializer):
    owner = DriverInformationSerializer(read_only=True)

    class Meta:
        model = ReplyDriver
        fields = ['id', 'order', 'created_at', 'owner']


class OrderDetailSerializer(serializers.ModelSerializer):
    order_files = OrderFilesSerializer(many=True)
    order_clicks = MyOrdersOtClicksSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'transport_type', 'name', 'location_from', 'location_to',
                  'date', 'weight', 'price', 'type_payment', 'description',
                  'created_at', 'updated_at', 'status', 'order_files', 'order_clicks']


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
