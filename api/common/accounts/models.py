import uuid
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ("Driver", 'Driver'),
        ("Client", 'Client'),
        ("Company", 'Company'),
        ("Administrator", 'Administrator')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=19, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE, max_length=20, default='Client')

    objects = AccountManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    @property
    def get_user_info(self):
        if self.role == 'Client':
            data = {
                'name': self.client_full_name.name,
                'avatar': self.client_avatar.image
            }
            return data
        if self.role == 'Company':
            data = {
                'name': self.logistic_company.company_name,
                'avatar': self.logistic_company.avatar
            }
            return data
        if self.role == 'Driver':
            data = {
                'name': self.driver_full_name.name,
                'avatar': self.driver_avatar.image
            }
            return data


class VerifyCode(models.Model):
    phone = models.CharField(max_length=22)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
