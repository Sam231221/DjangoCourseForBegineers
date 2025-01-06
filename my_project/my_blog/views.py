from django.shortcuts import render


# Create your views here.
def blog_listing_view(request):
    return render(request, "blog/blog_listing.html")
