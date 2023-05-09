from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=13, blank=True, validators=[RegexValidator(r"\d{2,3}-\d{3,4}-\d{4}")]
    )
    gender = models.CharField(
        max_length=1,
        blank=True,
        choices=GenderChoice.choices,
        default=GenderChoice.MALE,
    )


# class Profile(models.Model):
#     pass
