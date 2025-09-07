from decimal import Decimal
from django.db import models

# Create your models here.

class Product(models.Model):
    """Product information, server-side price authoritative."""
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.price})"


class Order(models.Model):
    """
    Each order stores the product, quantity, the price_at_purchase (unit price),
    and a calculated total_price. We store price_at_purchase to keep historical
    accuracy if product price later changes.
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Always compute total server-side (do not rely on client data)
        if not self.price_at_purchase:
            self.price_at_purchase = self.product.price
        # Use Decimal arithmetic and quantize to 2 decimals
        self.total_price = (self.price_at_purchase * Decimal(self.quantity)).quantize(Decimal('0.01'))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} {self.quantity}x {self.product.name} = {self.total_price}"