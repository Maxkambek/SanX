from rest_framework import generics, status, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.common.accounts.models import Account, VerifyCode
from api.common.main.models import Location, Country, FAQ
from api.tools.send_sms import send_sms
from .serializers import CountrySerializer, FAQSerializer, RegisterSerializer, LoginSerializer, LocationSerializer, \
    VerifyCodeSerializer, LoginVerifySerializer
from random import randint


class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = Account.objects.filter(phone=request.data['phone']).first()
        if phone:
            return Response({"message": "This number is already registered"}, status=400)
        verify = VerifyCode.objects.filter(phone=request.data['phone']).first()
        if verify:
            verify.delete()
        verification_code = str(randint(10000, 100000))
        send_sms(request.data['phone'], verification_code)
        VerifyCode.objects.create(phone=request.data['phone'], code=verification_code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class CheckVerifyCodeAPIView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        code = request.data['code']
        role = request.data['role']
        verify = VerifyCode.objects.filter(phone=phone, code=code).first()
        if not verify:
            return Response({"message": "The confirmation code is  incorrect!"}, status=404)
        verify.delete()
        user = Account.objects.create(
            phone=phone,
            role=role,
            password="12345678",
            is_active=True
        )
        user.save()
        return Response({
            "message": "User successfully registered",
            "token": user.tokens,
            "user_id": user.id
        }, status=201)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = Account.objects.filter(phone=request.data['phone']).first()
        if not phone:
            return Response({"message": "This number is not registered"}, status=404)
        verify = VerifyCode.objects.filter(phone=phone).first()
        if verify:
            verify.delete()
        verification_code = str(randint(10000, 100000))
        send_sms(request.data['phone'], verification_code)
        VerifyCode.objects.create(phone=request.data['phone'], code=verification_code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class LoginVerifyAPIView(generics.GenericAPIView):
    serializer_class = LoginVerifySerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        code = request.data['code']
        verify = VerifyCode.objects.filter(phone=phone, code=code).first()
        if not verify:
            return Response({"message": "The confirmation code is  incorrect!"}, status=404)
        verify.delete()
        user = Account.objects.filter(phone=phone).first()
        return Response({
            "message": "User successfully verified",
            "token": user.tokens,
            "user_id": user.id
        }, status=200)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#
# class DeleteAccountView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#     def delete(self, request, *args, **kwargs):
#         user = self.request.user
#         user.
