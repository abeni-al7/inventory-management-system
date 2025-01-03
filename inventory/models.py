from django.db import models
from django.core.validators import RegexValidator

class Suppliers(models.Model):
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r"^(9|7)\d{8}$", message="Phone number must be entered in the format: '912345678 / 712345678'. Up to 9 digits allowed.")
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=125)
    logo_url = models.URLField(blank=True)
    type = models.TextField(max_length=125, blank=True)

    def __str__(self):
        return self.name