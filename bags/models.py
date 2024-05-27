from django.db import models
from humans.models import Human
from products.models import Product


class WishList(object):
    human = models.ForeignKey("Human", on_delete=models.CASCADE)
    wished_item = models.ForeignKey("Product", on_delete=models.CASCADE)
    slug = models.SlugField(
        db_index=True, max_length=255, unique=True, primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"
        ordering = [
            "created_at",
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}").lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.human} - WishList"
