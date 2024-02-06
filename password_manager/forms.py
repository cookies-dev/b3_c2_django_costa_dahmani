from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Site


class SiteForm(forms.ModelForm):
    """
    Form used for creating or updating a Site object.
    """

    class Meta:
        model = Site
        fields = ["name", "url", "username", "password"]
