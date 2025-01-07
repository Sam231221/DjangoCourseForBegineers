from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("about/", views.about_view, name="about_view"),
    path("services/", views.services_view, name="services_view"),
    path("profile/", views.profile_view, name="profile_view"),
]
