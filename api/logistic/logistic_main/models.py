from django.db import models
from api.common.accounts.models import Account
from api.logistic.logistic_auth.models import LogisticCompany


class Story(models.Model):
    company = models.ForeignKey(LogisticCompany, on_delete=models.CASCADE, related_name='stories')
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company.company_name

    @property
    def company_infos(self):
        data = {
            "company_name": self.company.company_name,
            "avatar": self.company.avatar
        }
        return data
