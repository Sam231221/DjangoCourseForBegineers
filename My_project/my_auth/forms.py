from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# forms.py
from django import forms
from django.core.exceptions import ValidationError


class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(label="New Email", required=True)
    confirm_email = forms.EmailField(label="Confirm New Email", required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get("new_email")
        confirm_email = cleaned_data.get("confirm_email")

        if new_email != confirm_email:
            raise ValidationError("The new email addresses do not match.")

        if User.objects.filter(email=new_email).exists():
            raise ValidationError("This email is already taken by another user.")

        return cleaned_data


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "password", "placeholder": "Enter a password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "password", "placeholder": "Reenter  the password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter a Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Provide your Email"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Enter a Password"}),
            "password2": forms.PasswordInput(
                attrs={"placeholder": "ReType the Password"}
            ),
        }

    def clean_username(self):
        name = self.cleaned_data.get("username")
        if len(name) <= 3:
            raise forms.ValidationError("Name is too Short")
        return name


class LogInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter you Username"}),
            "password": forms.PasswordInput(
                attrs={"class": "password", "placeholder": "Enter your Password"}
            ),
        }
