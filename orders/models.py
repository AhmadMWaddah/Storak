from django.db import models
from humans.humans import Human
from bags.models import BagItem


class Order(models.Model):
    human = models.ForeignKey("humans.Human", on_delete=models.CASCADE)
    price = models.DecimalField(db_index=True, max_digits=8, decimal_places=2)
    items = models.ManyToManyField("bags.BagItem", through="OrderItem")
    total = models.DecimalField(db_index=True, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.human.full_name} Order"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    bag_item = models.ForeignKey("bags.BagItem", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(db_index=True, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        ordering = [
            "order",
            "bag_item",
        ]

    def __str__(self):
        return f"{self.item.name} X {self.quantity}"
