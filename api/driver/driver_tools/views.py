from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.driver.driver_tools.calculate import filter_nearby_locations
from .models import DriverWishlist, DriverCurrentLocation
from .serializers import WishListSerializer, WishlistCreateSerializer, DriverCurrentLocationSerializer


class WishlistListAPIView(generics.ListAPIView):
    queryset = DriverWishlist.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return DriverWishlist.objects.filter(user=self.request.user)


class AddToWishlistAPIView(generics.CreateAPIView):
    queryset = DriverWishlist.objects.all()
    serializer_class = WishlistCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        order_id = self.request.data.get('order')
        if DriverWishlist.objects.filter(user=self.request.user, order_id=order_id).first():
            return Response({'message': 'Already exists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class DeleteFromWishlistAPIView(generics.DestroyAPIView):
    queryset = DriverWishlist.objects.all()
    serializer_class = WishlistCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, *args, **kwargs):
        instance = DriverWishlist.objects.get(user_id=self.request.user.id, order_id=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class DriverCurrentLocationAPIView(generics.ListAPIView):
    serializer_class = DriverCurrentLocationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        long = self.request.query_params.get('long')
        return filter_nearby_locations(float(lat), float(long))


class DriverCurrentLocationChangeAPIView(generics.UpdateAPIView):
    serializer_class = DriverCurrentLocationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = DriverCurrentLocation.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = DriverCurrentLocation.objects.filter(user=self.request.user)
        if not instance:
            instance = DriverCurrentLocation.objects.create(longitude=request.data.get('longitude'),
                                                            latitude=request.data.get('latitude'),
                                                            user_id=self.request.user.id)
            instance.save()
        instance = DriverCurrentLocation.objects.filter(user=self.request.user).first()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
