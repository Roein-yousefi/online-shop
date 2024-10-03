from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, verbose_name=_('paid'))

    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=11, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=1000, verbose_name=_('Address'))

    order_notes = models.CharField(max_length=1000, verbose_name=_('Order Notes') , blank=True)

    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Oreder {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} for {self.product}'