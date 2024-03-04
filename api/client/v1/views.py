from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.client.client_auth.models import ClientAvatar, ClientDateBirth, ClientFullName
from . import serializers
from api.client.client_main.models import Order, ReplyDriver, ClientWishList
from .calculate import filter_nearby_locations_order
from .serializers import ClientWishListCreateSerializer, ClientWishListSerializer, ClientProfileSerializer, \
    ClientProfileChangeSerializer
from ...common.accounts.models import Account
from django.db.models import Q

from ...tools.pagination import LargeResultsSetPagination


class ClientFullNameCreateAPIView(generics.CreateAPIView):
    queryset = ClientFullName.objects.all()
    serializer_class = serializers.ClientFullNameSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if ClientFullName.objects.filter(user=self.request.user).first():
            q = ClientFullName.objects.filter(user=self.request.user).first()
            q.delete()
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


class ClientFullNameRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ClientFullName.objects.all()
    serializer_class = serializers.ClientFullNameSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        instance = ClientFullName.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = ClientFullName.objects.get(user=self.request.user)
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


class ClientAvatarCreateAPIView(generics.CreateAPIView):
    queryset = ClientAvatar.objects.all()
    serializer_class = serializers.ClientAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if ClientAvatar.objects.filter(user=self.request.user).first():
            q = ClientAvatar.objects.filter(user=self.request.user).first()
            q.delete()
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


class ClientAvatarRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ClientAvatar.objects.all()
    serializer_class = serializers.ClientAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        instance = ClientAvatar.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = ClientAvatar.objects.get(user=self.request.user)
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


class ClientDateBirthCreateAPIView(generics.CreateAPIView):
    queryset = ClientDateBirth.objects.all()
    serializer_class = serializers.ClientDateBirthSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if ClientDateBirth.objects.filter(user=self.request.user).first():
            q = ClientDateBirth.objects.filter(user=self.request.user).first()
            q.delete()
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


class ClientDateBirthRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ClientDateBirth.objects.all()
    serializer_class = serializers.ClientDateBirthSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        instance = ClientDateBirth.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = ClientDateBirth.objects.get(user=self.request.user)
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


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.views += 1
        instance.save()
        if self.request.user == instance.owner:
            return Response({'Permission Denied': 'You cannot edit this'}, status=status.HTTP_400_BAD_REQUEST)
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


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


class ReplyDriverCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ReplyDriverSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = ReplyDriver.objects.all()

    def create(self, request, *args, **kwargs):
        reply_driver = ReplyDriver.objects.filter(
            owner=self.request.user,
            order_id=self.request.data['order']
        ).first()
        if reply_driver:
            return Response({'message': "Already clicked"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ReplyDriverListAPIViewForClient(generics.ListAPIView):
    serializer_class = serializers.MyOrdersOtClicksSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        order = self.request.query_params.get('order_id')
        queryset = ReplyDriver.objects.filter(order_id=order)
        return queryset


class ReplyDriverListAPIViewForDriver(generics.ListAPIView):
    serializer_class = serializers.MyClicksSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = ReplyDriver.objects.filter(owner=self.request.user)
        return queryset


class GiveWorkAPIViewForClient(generics.GenericAPIView):
    serializer_class = serializers.GiveWorkSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        worker_id = self.request.data.get('worker_id')
        order_id = self.request.data.get('order_id')
        order = Order.objects.filter(id=order_id).first()
        user = Account.objects.filter(id=worker_id).first()
        if not user:
            return Response({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        if order is None:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        order.worker_id = user
        order.save()
        return Response({'message': 'Order saved'}, status=status.HTTP_200_OK)


class OrderListViewForMap(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        return filter_nearby_locations_order(lat, lon)


class ClientWishlistListAPIView(generics.ListAPIView):
    queryset = ClientWishList.objects.all()
    serializer_class = ClientWishListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return ClientWishList.objects.filter(user=self.request.user)


class ClientAddToWishlistAPIView(generics.CreateAPIView):
    queryset = ClientWishList.objects.all()
    serializer_class = ClientWishListCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        order_id = self.request.data.get('driver')
        if ClientWishList.objects.filter(user=self.request.user, driver__id=order_id).first():
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


class ClientDeleteFromWishlistAPIView(generics.DestroyAPIView):
    queryset = ClientWishList.objects.all()
    serializer_class = ClientWishListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, *args, **kwargs):
        instance = ClientWishList.objects.get(user_id=self.request.user.id, driver__id=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class FilterOrderListAPIView(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        search = self.request.query_params.get('search')
        weight_from = self.request.query_params.get('weight_from')
        weight_to = self.request.query_params.get('weight_to')
        location_from = self.request.query_params.get('location_from')
        location_to = self.request.query_params.get('location_to')
        volume_from = self.request.query_params.get('volume_from')
        volume_to = self.request.query_params.get('volume_to')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        type_payment = self.request.query_params.get('type_payment')
        price_from = self.request.query_params.get('price_from')
        price_to = self.request.query_params.get('price_to')
        search_con = Q()
        if search:
            search_con = Q(name__icontains=search)
        weight_from_con = Q()
        if weight_from:
            weight_from_con = Q(weight__gt=weight_from)
        weight_to_con = Q()
        if weight_to:
            weight_to_con = Q(weight__lt=weight_to)
        location_from_con = Q()
        if location_from:
            location_from_con = Q(location_from_id=location_from)
        location_to_con = Q()
        if location_to:
            location_to_con = Q(location_to_id=location_to)
        volume_from_con = Q()
        if volume_from:
            volume_from_con = Q(volume_m3__gt=volume_from)
        volume_to_con = Q()
        if volume_to:
            volume_to_con = Q(volume_m3__lt=volume_to)
        date_from_con = Q()
        if date_from:
            date_from_con = Q(date__gt=date_from)
        date_to_con = Q()
        if date_to:
            date_to_con = Q(date__lt=date_to)
        type_payment_con = Q()
        if type_payment:
            type_payment_con = Q(type_payment=type_payment)
        price_from_con = Q()
        if price_from:
            price_from_con = Q(price__gt=price_from)
        price_to_con = Q()
        if price_to:
            price_to_con = Q(price__lt=price_to)
        queryset = Order.objects.filter(search_con, weight_from_con, weight_to_con, location_from_con, location_to_con,
                                        volume_from_con, volume_to_con, date_from_con, date_to_con, type_payment_con,
                                        price_from_con, price_to_con)
        return queryset


class ClientProfileAPIView(generics.ListAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        account = Account.objects.filter(id=self.request.user.id)
        return account


class ClientProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ClientProfileChangeSerializer
    queryset = Account.objects.all()

    def update(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        name = self.request.data['name']
        lastname = self.request.data['last_name']
        surname = self.request.data['surname']
        date_birth = self.request.data['date_birth']
        avatar = self.request.data['avatar']
        bio = self.request.data['bio']
        instance = Account.objects.filter(id=self.request.user.id).first()
        if phone:
            instance.phone = phone
            instance.save()
        if bio:
            instance.bio = bio
            instance.save()
        cfl = ClientFullName.objects.filter(user=self.request.user).first()
        if cfl and name and surname and lastname:
            cfl.name = name
            cfl.surname = surname
            cfl.last_name = lastname
            cfl.save()
        ddb = ClientDateBirth.objects.filter(user=self.request.user).first()
        if ddb and date_birth:
            ddb.date = date_birth
            ddb.save()
        dd = ClientAvatar.objects.filter(user=self.request.user).first()
        if dd and avatar:
            dd.avatar = avatar
            dd.save()
        return Response({'message': 'Successfully updated'}, status=200)
