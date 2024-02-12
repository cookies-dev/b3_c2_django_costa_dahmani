from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Site


class SignupForm(UserCreationForm):
    """
    Form used for user signup.

    Inherits from UserCreationForm and adds fields for username, password1, and password2.
    """

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(forms.Form):
    """
    A form for user login.

    This form is used to collect the username and password from the user for authentication.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SiteForm(forms.ModelForm):
    """
    Form used for creating or updating a Site object.
    """

    class Meta:
        model = Site
        fields = ["name", "url", "username", "password"]