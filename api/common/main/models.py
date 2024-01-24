from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=223)
    flag_img = models.ImageField(upload_to='flags/')

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
