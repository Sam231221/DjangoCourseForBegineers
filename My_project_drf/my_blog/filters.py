from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter()  # Allows filtering by a price range
    name = filters.CharFilter(
        lookup_expr="icontains"
    )  # Case-insensitive search for product name
    category = filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )  # Category name filter

    class Meta:
        model = Product
        fields = ["price", "name", "category"]
