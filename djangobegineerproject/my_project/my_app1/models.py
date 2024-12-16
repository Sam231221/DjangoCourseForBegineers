from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)