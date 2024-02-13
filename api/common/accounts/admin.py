from django.contrib import admin

from .models import VerifyCode, Account
from ..main.models import Location, Country, Chat, ChatMessage, VersionProject

admin.site.register(VerifyCode)


@admin.register(VersionProject)
class VersionProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['phone', 'id']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
