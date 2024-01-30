from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=223)
    flag_img = models.ImageField(upload_to='flags/')
    code = models.CharField(max_length=10, null=True)

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

