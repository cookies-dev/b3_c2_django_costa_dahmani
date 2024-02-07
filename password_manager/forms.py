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

class SiteForm(forms.ModelForm):
    """
    Form used for creating or updating a Site object.
    """

    class Meta:
        model = Site
        fields = ["name", "url", "username", "password"]
