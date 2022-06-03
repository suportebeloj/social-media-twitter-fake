from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus":True,
        "class": "form-control mt-4",
        "placeholder": "Username"
    }), label="")
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class": "form-control",
            "placeholder": "password"
            }),
    )

class CustomCreationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus":True,
        "class": "form-control mt-4",
        "placeholder": "Username"
    }), label="")

    email = forms.CharField(label="", widget=forms.EmailInput(attrs={
        "autocomplete": "email",
        "class": "form-control",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(
        label="",
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "placeholder": "Password",
            "data-bs-toggle": "tooltip",
            "data-bs-html":"true",
            "data-bs-placement": "left",
            "title": password_validation.password_validators_help_text_html()
            }),
    )
    password2 = forms.CharField(
        label="",
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "placeholder": "Confirm password",
            "data-bs-toggle": "tooltip",
            "data-bs-html":"true",
            "data-bs-placement": "left",
            "title": _("Enter the same password as before, for verification.")
            }),
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")