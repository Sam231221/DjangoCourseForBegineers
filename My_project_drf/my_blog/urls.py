from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import BlogListView, ProductListView, UserDetailView

urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blog-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("user/", UserDetailView.as_view(), name="user_detail"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
