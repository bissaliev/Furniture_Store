from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField("Аватар", null=True, blank=True, upload_to="users")
    phone_number = models.CharField(
        "Номер телефона", max_length=10, blank=True, null=True
    )

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
