from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Site

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
