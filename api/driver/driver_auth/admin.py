from django.contrib import admin
from .models import TransportWeightType, TransportType, ModelTransport, ManufacturerType, ColorTransport


@admin.register(TransportWeightType)
class TransportWeightTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ManufacturerType)
class ManufacturerTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelTransport)
class ModelTransportAdmin(admin.ModelAdmin):
    pass


@admin.register(ColorTransport)
class ColorTransportAdmin(admin.ModelAdmin):
    pass
