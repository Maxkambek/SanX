from rest_framework import generics, permissions, status
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from . import serializers
from rest_framework.response import Response

from .serializers import DriverProfileSerializer, DriverProfileChangeSerializer


class DriverFullNameCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverFullNameSerializer
    queryset = DriverFullName.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverFullName.objects.filter(user=self.request.user).first()
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


class DriverFullNameRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverFullNameSerializer
    queryset = DriverFullName.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverFullName.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = DriverFullName.objects.get(user=self.request.user)
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


class DriverDateBirthCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverDateBirthSerializer
    queryset = DriverDateBirth.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverDateBirth.objects.filter(user=self.request.user).first()
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


class DriverDateBirthRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DriverDateBirth.objects.all()
    serializer_class = serializers.DriverDateBirthSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverDateBirth.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = DriverDateBirth.objects.get(user=self.request.user)
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


class DriverDirectionCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverDirectionSerializer
    queryset = DriverDirection.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverDirection.objects.filter(user=self.request.user).first()
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


class DriverDirectionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverDirectionSerializer
    queryset = DriverDirection.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverDirection.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverDirection.objects.get(user=self.request.user)
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


class DriverAvatarCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverAvatarSerializer
    queryset = DriverAvatar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverAvatar.objects.filter(user=self.request.user).first()
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


class DriverAvatarRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DriverAvatar.objects.all()
    serializer_class = serializers.DriverAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverAvatar.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverAvatar.objects.get(user=self.request.user)
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


class DriverPassportCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverPassportSerializer
    queryset = DriverPassport.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverPassport.objects.filter(user=self.request.user).first()
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


class DriverPassportRUDAPIView(generics.RetrieveUpdateAPIView):
    queryset = DriverPassport.objects.all()
    serializer_class = serializers.DriverPassportSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverPassport.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverPassport.objects.get(user=self.request.user)
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


class DriverLicenseCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverLicenseSerializer
    queryset = DriverLicense.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverLicense.objects.filter(user=self.request.user).first()
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


class DriverLicenseRUDAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverLicenseSerializer
    queryset = DriverLicense.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverLicense.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverLicense.objects.get(user=self.request.user)
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


class DriverCompanyCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverCompanySerializer
    queryset = DriverCompany.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverCompany.objects.filter(user=self.request.user).first()
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


class DriverCompanyRUDAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverCompanySerializer
    queryset = DriverCompany.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverCompany.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverCompany.objects.get(user=self.request.user)
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


class DriverPaymentTypeCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverPaymentTypeSerializer
    queryset = DriverPaymentType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverPaymentType.objects.filter(user=self.request.user).first()
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


class DriverPaymentTypeRUDAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverPaymentTypeSerializer
    queryset = DriverPaymentType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverPaymentType.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverPaymentType.objects.get(user=self.request.user)
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


class DriverTransportDetailsCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverTransportDetailsSerializer
    queryset = DriverTransportDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = DriverTransportDetails.objects.filter(user=self.request.user).first()
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


class DriverTransportDetailsRUDAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DriverTransportDetailsSerializer
    queryset = DriverTransportDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = DriverTransportDetails.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = DriverTransportDetails.objects.get(user=self.request.user)
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


class TechnicalPassportCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TechnicalPassportSerializer
    queryset = TechnicalPassport.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = TechnicalPassport.objects.filter(user=self.request.user).first()
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


class TechnicalPassportRUDAPIView(generics.RetrieveUpdateAPIView):
    queryset = TechnicalPassport.objects.all()
    serializer_class = serializers.TechnicalPassportSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = TechnicalPassport.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = TechnicalPassport.objects.get(user=self.request.user)
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


class TransportImagesCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TransportImagesSerializer
    queryset = TransportImages.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            q = TransportImages.objects.filter(user=self.request.user).first()
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


class TransportImagesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.TransportImagesSerializer
    queryset = TransportImages.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        instance = TransportImages.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not self.queryset.filter(user=self.request.user):
            return Response({'message': 'First create before '}, status=status.HTTP_404_NOT_FOUND)
        partial = kwargs.pop('partial', False)
        instance = TransportImages.objects.get(user=self.request.user)
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


class TransportWeightTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.TransportWeightTypeSerializer
    queryset = TransportWeightType.objects.all()


class TransportTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.TransportTypeSerializer

    def get_queryset(self):
        filter_id = self.request.GET.get('filter_id')
        print(filter_id)
        queryset = TransportType.objects.all()
        if filter_id:
            queryset = queryset.filter(transport_wight_id=filter_id)
        return queryset


class ManufacturerTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.ManufacturerSerializer
    queryset = ManufacturerType.objects.all()


class ModelTransportTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.ModelTransportSerializer

    def get_queryset(self):
        pk = self.request.GET.get('filter_id')
        queryset = ModelTransport.objects.all()
        if pk:
            queryset = queryset.filter(manufacturer_id=pk)
        return queryset


class ColorTransportListAPIView(generics.ListAPIView):
    serializer_class = serializers.ColorTransportSerializer
    queryset = ColorTransport.objects.all()


class DriverCheckAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        passport = DriverPassport.objects.filter(user=self.request.user).first()
        lice = DriverLicense.objects.filter(user=self.request.user).first()
        company = DriverCompany.objects.filter(user=self.request.user).first()
        payment = DriverPaymentType.objects.filter(user=self.request.user).first()
        detail = DriverTransportDetails.objects.filter(user=self.request.user).first()
        tec_pas = TechnicalPassport.objects.filter(user=self.request.user).first()
        images = TransportImages.objects.filter(user=self.request.user).first()
        data = {
            'passport': True if passport else False,
            'license': True if lice else False,
            'company': True if company else False,
            'payment': True if payment else False,
            'transport_detail': True if detail else False,
            'tech_passport': True if tec_pas else False,
            'images': True if images else False
        }
        return Response(data, status=200)


class DriverProfileGetView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = DriverProfileSerializer

    def get_queryset(self):
        account = Account.objects.filter(id=self.request.user.id)
        return account


class DriverProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = DriverProfileChangeSerializer
    queryset = Account.objects.all()

    def update(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        name = self.request.data['name']
        lastname = self.request.data['last_name']
        surname = self.request.data['surname']
        date_birth = self.request.data['date_birth']
        direction_from = self.request.data['direction_from']
        direction_to = self.request.data['direction_to']
        bio = self.request.data['bio']
        instance = Account.objects.filter(id=self.request.user.id).first()
        if phone:
            instance.phone = phone
            instance.bio = bio
            instance.save()
        dfl = DriverFullName.objects.filter(user=self.request.user).first()
        if dfl and name and surname and lastname:
            dfl.name = name
            dfl.surname = surname
            dfl.last_name = lastname
            dfl.save()
        ddb = DriverDateBirth.objects.filter(user=self.request.user).first()
        if ddb and date_birth:
            ddb.date = date_birth
            ddb.save()
        dd = DriverDirection.objects.filter(user=self.request.user).first()
        if dd and direction_from and direction_to:
            dd.direction_from = direction_from
            dd.direction_to = direction_to
            dd.save()
        return Response({'message': 'Successfully updated'}, status=200)
