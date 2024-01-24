from django.db import models
from api.common.accounts.models import Account
from api.common.main.models import Location
from api.driver.driver_auth.models import TransportType


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Completed', 'Completed')
    )
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_orders')
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE)
    name = models.CharField(max_length=333)
    location_from = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_to = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    type_payment = models.CharField(max_length=123)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=123, default='New')
    latitude = models.DecimalField(max_digits=20, decimal_places=6)
    longitude = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.name


class ReplyDriver(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='driver_click')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_clicks')
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.BooleanField(default=False)

    def __str__(self):
        return self.order.name
