from django.urls import path
from . import views

app_name = "my_blog"

urlpatterns = [
    path("", views.blog_listing_view, name="blog_listing_view"),
    path("<slug:slug>/", views.blog_detail_view, name="blog_detail_view"),
]
