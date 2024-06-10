from django.db import models
from humans.models import Human
from products.models import Product


class BagItem(models.Model):
    human = models.ForeignKey("humans.Human", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = [
            "created_at",
        ]

    def __str__(self):
        return f"{self.human.full_name} - {self.product.name} ({self.quantity})"
