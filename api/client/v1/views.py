from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.client.client_auth.models import ClientAvatar, ClientDateBirth, ClientFullName
from . import serializers


class ClientFullNameCreateAPIView(generics.CreateAPIView):
    queryset = ClientFullName.objects.all()
    serializer_class = serializers.ClientFullNameSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if ClientFullName.objects.get(user=self.request.user):
            return Response({'message': "Already exists"}, status=status.HTTP_409_CONFLICT)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

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
        if ClientAvatar.objects.get(user=self.request.user):
            return Response({'message': "Already exists"}, status=status.HTTP_409_CONFLICT)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

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


class ClientDateBirthCreateAPIView(generics.CreateAPIView):
    queryset = ClientDateBirth.objects.all()
    serializer_class = serializers.ClientDateBirthSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if ClientDateBirth.objects.get(user=self.request.user):
            return Response({'message': "Already exists"}, status=status.HTTP_409_CONFLICT)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
