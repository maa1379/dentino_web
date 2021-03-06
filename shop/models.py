from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=125)
    icon = models.ImageField(upload_to="image/category/icon/", blank=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="sub"
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sell = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    discount_percent = models.IntegerField()
    image = models.ImageField(upload_to="images/produce/")
    image2 = models.ImageField(upload_to="images/produce/", blank=True)
    image3 = models.ImageField(upload_to="images/produce/", blank=True)
    image4 = models.ImageField(upload_to="images/produce/", blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="produce"
    )

    def save(self, *args, **kwargs):
        count = (self.price * self.discount_percent) / 100
        self.sell = self.price - count
        return super(Product, self).save()

    def __str__(self):
        return self.name
