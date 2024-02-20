from django.db import models

from api.common.accounts.models import Account


class Category(models.Model):
    name = models.CharField(max_length=233)
    description = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=223)
    flag_img = models.URLField(null=True, blank=True)
    code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=233)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=223)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=233)
    answer = models.CharField(max_length=444)

    def __str__(self):
        return self.question


class News(models.Model):
    file = models.FileField(upload_to='news/')
    title = models.CharField(max_length=444)
    content = models.TextField()
    sub_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Banners(models.Model):
    title = models.CharField(max_length=333)
    description = models.CharField(max_length=333, null=True, blank=True)
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chat(models.Model):
    participant1 = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='participant1')
    participant2 = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='participant2')


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    receiver = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, related_name='sender')
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']


class VersionProject(models.Model):
    STATUS = (
        ('Optional', 'Optional'),
        ('Forced', 'Forced'),
        ('Shutdown', 'Shutdown')
    )
    version = models.PositiveIntegerField()
    version_text = models.CharField(max_length=333)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=123, choices=STATUS)

    def __str__(self):
        return self.version_text
