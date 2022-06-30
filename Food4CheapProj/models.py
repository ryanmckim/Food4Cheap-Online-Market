from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductType(models.TextChoices):
    BAKED_GOOD = 1, _("baked good")
    DAIRY = 2, _("dairy")
    FRUIT = 3, _("fruit")
    MEAT = 4, _("meat")
    SEAFOOD = 5, _("seafood")
    VEGETABLE = 6, _("vegetable")


class Category(models.Model):
    name = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=ProductType.choices)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255, choices=ProductType.choices)
    image_url = models.ImageField(null=True, blank=True)

    measurement = models.CharField(max_length=255)
    serving_size = models.CharField(max_length=255)
    calories = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    carbohydrates = models.CharField(max_length=255)
    proteins = models.CharField(max_length=255)


class CartItem(models.Model):
    times_bought = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
