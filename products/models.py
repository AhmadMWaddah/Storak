from datetime import datetime
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.validators import MinValueValidator


def set_default_image(model_name):
    """
    Usage: set_default_image("category")
    """
    base_path = "defaults/"
    if model_name == "line":
        return base_path + "LineImage.png"
    elif model_name == "category":
        return base_path + "CategoryImage.png"
    elif model_name == "product":
        return base_path + "ProductImage.png"
    else:
        raise ValueError(f"Invalid model name: {model_name}")


def get_upload_path(instance, filename):
    now = datetime.now().strftime("%Y/%m/%d")
    saving_directory = instance._meta.verbose_name_plural.lower()
    return f"{saving_directory}/{instance.slug}/{now}/{filename}"


class Line(models.Model):
    name = models.CharField(db_index=True, max_length=255, unique=True)
    slug = models.SlugField(
        db_index=True, max_length=255, unique=True, primary_key=True
    )
    image = models.ImageField(
        upload_to=get_upload_path, default=set_default_image("line")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Line"
        verbose_name_plural = "Lines"
        ordering = [
            "name",
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}").lower()

        super(Line, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    line = models.ForeignKey("Line", on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=255, unique=True)
    slug = models.SlugField(
        db_index=True, max_length=255, unique=True, primary_key=True
    )
    description = models.TextField(default="", blank=True, null=True)
    image = models.ImageField(
        upload_to=get_upload_path,
        default=set_default_image("category"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}").lower()

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    BEST_SELLER = "BSR"
    FEATURED = "FTD"
    TRENDING = "TND"
    CLEARANCE = "CLS"
    TAGS_CHOICES = [
        (BEST_SELLER, "Best Seller"),
        (FEATURED, "Featured"),
        (TRENDING, "Trending"),
        (CLEARANCE, "Clearance"),
    ]
    line = models.ForeignKey("Line", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=255, unique=True)
    slug = models.SlugField(
        db_index=True, max_length=255, unique=True, primary_key=True
    )
    description = models.TextField(default="", blank=True, null=True)
    sku = models.CharField(db_index=True, max_length=15, unique=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price_before = models.DecimalField(
        db_index=True, max_digits=6, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(db_index=True, max_digits=6, decimal_places=2)
    tag = models.CharField(
        db_index=True, max_length=12, choices=TAGS_CHOICES, null=True, blank=True
    )
    image = models.ImageField(
        upload_to=get_upload_path,
        default=set_default_image("product"),
    )
    image_two = models.ImageField(
        upload_to=get_upload_path,
        default=set_default_image("product"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def is_available(self):
        if self.quantity > 0:
            return True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.sku}").lower()

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
