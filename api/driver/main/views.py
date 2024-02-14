from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import DriverWishlist
from .serializers import WishListSerializer, WishlistCreateSerializer


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
