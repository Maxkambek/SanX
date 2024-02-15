from django.db import models
from api.common.accounts.models import Account
from api.common.main.models import Location, District
from api.driver.driver_auth.models import TransportType
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myMahkamApps")


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Completed', 'Completed')
    )
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_orders')
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE, related_name="order_transport_type")
    name = models.CharField(max_length=333)
    location_from = models.ForeignKey(District, on_delete=models.CASCADE, related_name="location_from_order", null=True)
    location_to = models.ForeignKey(District, on_delete=models.CASCADE, related_name="location_to_order", null=True)
    date = models.DateField()
    weight = models.PositiveIntegerField(default=0)
    volume_m3 = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    type_payment = models.CharField(max_length=123)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=123, default='New')
    worker_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        location = geolocator.geocode(f"{self.location_from.name}, {self.location_from.country.name}")
        self.longitude = location.longitude
        self.latitude = location.latitude


class OrderFiles(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_files')
    file = models.FileField(upload_to='orders/')


class ReplyDriver(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='driver_click')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_clicks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.name
