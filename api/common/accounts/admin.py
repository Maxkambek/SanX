from django.contrib import admin

from .models import VerifyCode, Account
from ..main.models import Location, Country

admin.site.register(VerifyCode)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['phone', 'id']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
