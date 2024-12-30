from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models
from products.models import Product

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SalesOrder(TimeStampedModel):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products: models.ManyToManyField[Product, SalesOrder] = models.ManyToManyField(
        Product
    )

    def __str__(self) -> str:
        return self.description
