from io import BytesIO
from PIL import Image
from django.db import models
from api.common.accounts.models import Account
from api.common.main.models import District, Country
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
    location_from = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="location_from_order", null=True)
    location_to = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="location_to_order", null=True)
    date = models.DateField()
    weight = models.PositiveIntegerField(default=0)
    volume_m3 = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(null=True)
    type_payment = models.CharField(max_length=123)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=123, default='New')
    worker_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=25, null=True, blank=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=25, null=True, blank=True)
    file_1 = models.FileField(upload_to='files/', null=True, blank=True)
    file_2 = models.FileField(upload_to='files/', null=True, blank=True)
    file_3 = models.FileField(upload_to='files/', null=True, blank=True)
    file_4 = models.FileField(upload_to='files/', null=True, blank=True)
    file_5 = models.FileField(upload_to='files/', null=True, blank=True)
    file_6 = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.name


class OrderFiles(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_files')
    file = models.FileField(upload_to='orders/')


class ReplyDriver(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='driver_click')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_clicks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_price = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.order.name


class Contracts(models.Model):
    contract_num = models.PositiveIntegerField(default=1000)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='contract_order')
    driver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='contract_driver')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.contract_num}'


class ClientWishList(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='client_wish_list')
    driver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='client_wish_list_driver')

    def __str__(self):
        return f'{self.user.phone}'


class DriverClientOrderContract(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='contract_order_id')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='contract_sender')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='contract_receiver')
    updated_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    @property
    def default_price(self):
        return self.order_id.price

    def __str__(self):
        return self.sender.phone
