from django.db import models
from my_auth.models import User


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer_profile"
    )
    full_name = models.CharField(max_length=200, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, max_length=200, null=True)
    category = models.CharField(
        max_length=100
    )  # You might replace this with a ForeignKey if you have a Category model.
    image = models.ImageField(upload_to="products/")
    marked_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    warranty = models.CharField(max_length=200, blank=True, null=True)
    return_policy = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    PAYMENT_METHODS = [
        ("COD", "Cash on Delivery"),
        ("ONLINE", "Online Payment"),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    ordered_by = models.CharField(max_length=200, null=True)
    shipping_address = models.TextField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.ordered_by}"
