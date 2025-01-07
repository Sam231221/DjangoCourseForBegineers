from django.contrib import admin
from .models import Category, Blog

# Register your models here.
admin.site.register((Category, Blog))
