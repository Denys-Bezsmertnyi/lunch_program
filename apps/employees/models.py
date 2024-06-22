from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone_number = models.CharField(max_length=20, help_text='Phone number in +380XXXXXXXXX format')
    age = models.PositiveIntegerField(blank=True, null=True)

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
    )

    def __str__(self):
        return f"{self.username}"
