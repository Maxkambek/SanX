from rest_framework import generics, status, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.common.accounts.models import Account, VerifyCode
from api.common.main.models import Location, Country, FAQ, News, Banners, ChatMessage, Chat, VersionProject
from api.tools.send_sms import send_sms
from .serializers import CountrySerializer, FAQSerializer, RegisterSerializer, LoginSerializer, LocationSerializer, \
    VerifyCodeSerializer, LoginVerifySerializer, NewsSerializer, BannersSerializer, VersionProjectSerializer
from random import randint

from ...tools.permissions import get_user_info


class VersionProjectListAPIView(generics.ListAPIView):
    serializer_class = VersionProjectSerializer
    queryset = VersionProject.objects.all()


class ChatCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        sender = self.request.user.id
        receiver = request.data['receiver']
        content = request.data['content']
        chat = Chat.objects.filter(participant1_id=sender, participant2_id=receiver).first()
        if chat is None:
            chat = Chat.objects.create(participant1_id=sender, participant2_id=receiver)
            chat.save()
        chat = Chat.objects.filter(participant1_id=sender, participant2_id=receiver).first()
        message = ChatMessage.objects.create(chat_id=chat.id, sender_id=sender, receiver_id=receiver, content=content)
        message.save()
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)


class ChatListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        data = []
        chats = Chat.objects.filter(participant1_id=request.user)
        for chat in chats:
            user = Account.objects.get(id=chat.participant2_id)
            data.append(dict(
                chat_id=chat.id,
                user_info=get_user_info(user),
            ))
        return Response(data)


class ChatDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        data = []
        msg = ChatMessage.objects.filter(chat_id=pk)
        for i in msg:
            data.append(dict(
                id=i.id,
                content=i.content
            ))
        return Response(data)


class BannersListAPIView(generics.ListAPIView):
    serializer_class = BannersSerializer
    queryset = Banners.objects.all()


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


# class DeleteAccountView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#     def delete(self, request, *args, **kwargs):
#         user = self.request.user
#         user.


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
