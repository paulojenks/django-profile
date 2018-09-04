from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, validators=[EmailValidator])
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, validators=[MinLengthValidator(10)])
    avatar = models.ImageField(upload_to="avatar_photos", default="avatar_photos/avatar-159236_1280.png")


