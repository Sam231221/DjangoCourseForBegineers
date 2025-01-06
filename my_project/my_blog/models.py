from django.db import models
from my_auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="blog_posts"
    )
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="blog_posts")
    tags = models.CharField(
        max_length=200, blank=True, help_text="Comma-separated tags"
    )
    featured_image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
