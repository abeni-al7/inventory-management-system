from django.contrib import admin
from .models import Categories, Manufacturer, Suppliers

admin.site.register(Suppliers)
admin.site.register(Categories)
admin.site.register(Manufacturer)