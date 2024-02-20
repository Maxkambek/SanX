from django.db import models
from api.common.accounts.models import Account
from api.common.main.models import Country, Location


class TransportWeightType(models.Model):
    name = models.CharField(max_length=123)
    description = models.CharField(max_length=233)

    def __str__(self):
        return self.name


class TransportType(models.Model):
    transport_wight = models.ForeignKey(TransportWeightType, on_delete=models.CASCADE,
                                        related_name="transport_weight_types")
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='transport_types')

    def __str__(self):
        return self.name


class ManufacturerType(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class ModelTransport(models.Model):
    manufacturer = models.ForeignKey(ManufacturerType, on_delete=models.CASCADE, related_name="manufacturer_types")
    name = models.CharField(max_length=123)
    description = models.CharField(max_length=233)

    def __str__(self):
        return self.name


class ColorTransport(models.Model):
    name = models.CharField(max_length=123)
    color = models.CharField(max_length=123)

    def __str__(self):
        return self.name


#

class DriverFullName(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_full_name")
    name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    surname = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class DriverDateBirth(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_date_birth")
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"


class DriverDirection(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_direction")
    direction_from = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="direction_from")
    direction_to = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="direction_to")

    def __str__(self):
        return f"{self.direction_from} {self.direction_to}"


class DriverAvatar(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_avatar")
    image = models.FileField(upload_to='driver/avatar/')

    def __str__(self):
        return f"{self.user.phone}"


class DriverPassport(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_passport")
    seria_num = models.CharField(max_length=12)
    front_side = models.FileField(upload_to='driver/passports/')
    with_residence = models.FileField(upload_to='driver/passports/')
    face_img = models.FileField(upload_to='driver/passports/', null=True, blank=True)

    def __str__(self):
        return self.user.phone


class DriverLicense(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_license")
    license_seria_num = models.CharField(max_length=23)
    license_expiration_date = models.CharField(max_length=123)
    front_side = models.FileField(upload_to='driver/license/')
    back_side = models.FileField(upload_to='driver/license/')
    face_img = models.FileField(upload_to='driver/license/', null=True, blank=True)

    def __str__(self):
        return self.user.phone


class DriverCompany(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_company")
    company_name = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name="company_company")


class DriverPaymentType(models.Model):
    TYPE_PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Transfer', 'Transfer')
    )
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_payment_type")
    payment_type = models.CharField(max_length=30, choices=TYPE_PAYMENT_CHOICES)


class DriverTransportDetails(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_transport_details")
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE)
    model_transport = models.ForeignKey(ModelTransport, on_delete=models.CASCADE)
    color_transport = models.ForeignKey(ColorTransport, on_delete=models.CASCADE)
    transport_made_date = models.CharField(max_length=45)
    tons_from = models.PositiveIntegerField()
    tons_to = models.PositiveIntegerField()
    volume3_from = models.PositiveIntegerField(null=True, blank=True)
    volume3_to = models.PositiveIntegerField(null=True, blank=True)


class TechnicalPassport(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_technical_passport")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=123)
    front_side_img = models.ImageField(upload_to='technical_passport/')
    back_side_img = models.ImageField(upload_to='technical_passport/')

    def __str__(self):
        return self.user.phone


class TransportImages(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver_transport_images")
    transport_front = models.FileField(upload_to='transport_images/')
    transport_left = models.FileField(upload_to='transport_images/')
    transport_behind = models.FileField(upload_to='transport_images/')
    transport_right = models.FileField(upload_to='transport_images')
    row_seats = models.FileField(upload_to='transport_images/')
    baggage = models.FileField(upload_to='transport_images/')

    def __str__(self):
        return self.user.phone
