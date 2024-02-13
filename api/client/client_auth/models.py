from django.db import models
from api.common.accounts.models import Account


class ClientFullName(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='client_full_name')
    name = models.CharField(max_length=233)
    last_name = models.CharField(max_length=233)
    surname = models.CharField(max_length=233)

    def __str__(self):
        return self.name


class ClientDateBirth(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return self.user.phone


class ClientAvatar(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='client_avatar')
    image = models.FileField(upload_to='client/avatars/')
