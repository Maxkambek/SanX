from rest_framework import generics, permissions, status
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from . import serializers
from rest_framework.response import Response


class DriverFullNameCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverFullNameSerializer
    queryset = DriverFullName.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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
        instance = DriverDirection.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
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
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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
        instance = DriverAvatar.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
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
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class DriverLicenseCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverLicenseSerializer
    queryset = DriverLicense.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class DriverCompanyCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverCompanySerializer
    queryset = DriverCompany.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class DriverPaymentTypeCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverPaymentTypeSerializer
    queryset = DriverPaymentType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class DriverTransportDetailsCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.DriverTransportDetailsSerializer
    queryset = DriverTransportDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class TechnicalPassportCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TechnicalPassportSerializer
    queryset = TechnicalPassport.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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


class TransportImagesCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TransportImagesSerializer
    queryset = TransportImages.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(user=self.request.user):
            return Response({'message': "Already Exists"}, status=status.HTTP_409_CONFLICT)
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
        instance = TransportImages.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
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
