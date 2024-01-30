from django.db import models
from api.common.accounts.models import Account
from api.common.main.models import Country


class LogisticCompany(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='logistic_company')
    passport_seria_number = models.CharField(max_length=123, null=True, blank=True)
    company_name = models.CharField(max_length=223)
    address = models.CharField(max_length=333, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=444, null=True, blank=True)
    company_phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.FileField(upload_to='logistic/logistic', null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Logistic Company'
        verbose_name_plural = 'Logistic Company'


