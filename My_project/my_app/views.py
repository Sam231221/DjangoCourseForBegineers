from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import (
    ContactForm,
    CheckoutForm,
    CustomerRegistrationForm,
    CustomerLoginForm,
    ProductForm,
    PasswordForgotForm,
    PasswordResetForm,
)
from .models import ContactSubmission


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def about_view(request):
    return HttpResponse("About Us")


def profile_view(request):
    return render(request, "profile.html", {})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database (optional)
            ContactSubmission.objects.create(**form.cleaned_data)
            return JsonResponse(
                {"success": True, "message": "Thank you for your message!"}
            )
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    form = ContactForm()
    checkoutform = CheckoutForm()
    customer_registration_form = CustomerRegistrationForm()
    customer_login_form = CustomerLoginForm()
    product_form = ProductForm()
    password_forgot_form = PasswordForgotForm()
    password_reset_form = PasswordResetForm()
    return render(
        request,
        "contact/contact.html",
        {
            "form": form,
            "checkoutform": checkoutform,
            "customer_registration_form": customer_registration_form,
            "customer_login_form": customer_login_form,
            "product_form": product_form,
            "password_forgot_form": password_forgot_form,
            "password_reset_form": password_reset_form,
        },
    )


def services_view(request):
    return HttpResponse("Services")


def blogs_view(request):
    return HttpResponse("Blogs")
