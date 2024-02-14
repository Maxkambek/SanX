from django.contrib import admin

from .models import Category, District


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

