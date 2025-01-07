from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q


def blog_listing_view(request):
    search_query = request.GET.get("search", "")
    page_number = request.GET.get("page", 1)

    # Filter blogs based on the search query
    if search_query:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
    else:
        blogs = Blog.objects.all()

    # Paginate the blogs
    paginator = Paginator(blogs, 3)  # Show 5 blogs per page
    page_obj = paginator.get_page(page_number)

    # Fetch recent and popular blogs
    recent_blogs = Blog.objects.order_by("-date_created")[:5]
    popular_blogs = Blog.objects.order_by("-views")[:5]

    context = {
        "blogs": page_obj,
        "recent_blogs": recent_blogs,
        "popular_blogs": popular_blogs,
        "search_query": search_query,
    }
    return render(request, "blogs/blog_listing.html", context)


def blog_detail_view(request, slug):
    # Get the blog post by slug
    blog = get_object_or_404(Blog, slug=slug)

    # Fetch recent and popular blogs (optional)
    recent_blogs = Blog.objects.order_by("-date_created")[:5]
    popular_blogs = Blog.objects.order_by("-views")[:5]

    context = {
        "blog": blog,
        "recent_blogs": recent_blogs,
        "popular_blogs": popular_blogs,
    }
    return render(request, "blogs/blog_detail.html", context)
