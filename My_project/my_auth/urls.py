from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views

app_name = "my_auth"

urlpatterns = [
    re_path(
        r"^accounts/register/$", views.RegistrationView.as_view(), name="register-view"
    ),
    re_path(r"^accounts/login/$", views.LoginView.as_view(), name="login-view"),
    re_path(r"^accounts/logout/$", views.logoutview, name="logout-view"),
    path(
        "activate/<uidb64>/<token>/",
        views.ActivateAccountView.as_view(),
        name="account-activation-view",
    ),
    re_path(
        r"^request-reset-password/$",
        views.RequestResetPasswordView.as_view(),
        name="request-reset-password-view",
    ),
    path(
        "set-new-password/<uidb64>/<token>/",
        views.SetNewPasswordView.as_view(),
        name="set-new-password-view",
    ),
    path("change-email/", views.ChangeEmailView.as_view(), name="change-email-view"),
    path(
        "confirm-email-change/<str:uidb64>/<str:token>/",
        views.Confirm_Email_Change_View.as_view(),
        name="confirm-email-change-view",
    ),
]
