from django.db import models
from api.client.client_main.models import Order
from api.common.accounts.models import Account


class DriverWishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='driver_wishlist')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='driver_wishlist')

    def __str__(self):
        return f'{self.user.phone}'


class DriverCurrentLocation(models.Model):
    STATUS = (
        ('Busy', 'Busy'),
        ('Free', 'Free')
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='drivers_location')
    longitude = models.DecimalField(max_digits=20, decimal_places=12)
    latitude = models.DecimalField(max_digits=20, decimal_places=12)
    status = models.CharField(max_length=20, choices=STATUS, default='Free')

    def __str__(self):
        return f'{self.user.phone}'
