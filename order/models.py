from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()
from shop.models import Product


# Create your models here.
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="items")


class Order(models.Model):
    user = models.ForeignKey(
        user, on_delete=models.SET_NULL, null=True, related_name="orders"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    code = models.CharField(max_length=125, null=True, blank=True)
    name = models.CharField(max_length=1250, null=True, blank=True)
    family = models.CharField(max_length=1250, null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=1250)
    authority = models.CharField(null=True, blank=True, max_length=100)
    is_send=models.BooleanField(default=False)

    def total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        return total
