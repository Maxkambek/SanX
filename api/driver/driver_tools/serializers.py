from .models import DriverWishlist, DriverCurrentLocation
from rest_framework import serializers
from api.client.v1.serializers import OrderSerializer


class WishListSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = DriverWishlist
        fields = ['id', 'order']


class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverWishlist
        fields = ['order']


class DriverCurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCurrentLocation
        fields = ['longitude', 'latitude', 'status']
