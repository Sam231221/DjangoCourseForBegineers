from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Blog
from .serializers import ProductSerializer, BlogSerializer
from .filters import ProductFilter
from .serializers import BlogSerializer
from .pagination import BlogPagination

from rest_framework.permissions import IsAuthenticated


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "username": user.username,
                "email": user.email,
            }
        )


# class BlogListView(ListAPIView):
#     queryset = Blog.objects.all().order_by("-created_at")
#     serializer_class = BlogSerializer
#     pagination_class = BlogPagination  # Use this if using custom pagination


class BlogListView(APIView):
    def get(self, request):
        queryset = Blog.objects.all().order_by("-date_created")
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Items per page
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
