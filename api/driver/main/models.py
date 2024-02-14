from django.db import models
from api.client.client_main.models import Order
from api.common.accounts.models import Account


class DriverWishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='driver_wishlist')
    order = models.ForeignKey(Order, on_delete=models, related_name='driver_wishlist')

    def __str__(self):
        return f'{self.user.phone}'

