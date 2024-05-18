from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.urls import reverse
from django.utils.text import slugify


class HumanManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, user_name, password=None):
        if not email:
            raise ValueError("E-Mail is Required, Please Provide Your E-Mail.")
        if not first_name:
            raise ValueError("E-Mail is Required, Please Provide Your First Name.")
        if not last_name:
            raise ValueError("E-Mail is Required, Please Provide Your Last Name.")
        if not user_name:
            raise ValueError("E-Mail is Required, Please Provide Your User Name.")
        user = self.model(
            email=self.normalize_email(email).lower(),
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, user_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Human(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="EMail", max_length=255, unique=True)
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    user_name = models.CharField(verbose_name="User Name", max_length=255)
    slug = models.SlugField(
        verbose_name="Slug", primary_key=True, unique=True, allow_unicode=True
    )
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "user_name",
    ]

    objects = HumanManager()

    def __str__(self):
        return f"{self.user_name} - {self.email}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.email}-{self.user_name}")

        super(Human, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Humans:HumanDetailsUrl", args=[f"{self.slug}"])
