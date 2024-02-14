from django.contrib import admin
from .models import LogisticCompany


@admin.register(LogisticCompany)
class LogisticCompanyAdmin(admin.ModelAdmin):
    pass
