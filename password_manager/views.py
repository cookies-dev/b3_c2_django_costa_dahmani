from multiprocessing.managers import BaseManager

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Site
from .forms import SiteForm, UserCreationForm, LoginForm


def site_list(request: HttpRequest) -> HttpResponse:
    """
    View function that displays a list of sites for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML template.
    """
    form = SiteForm(request.POST)
    sites: BaseManager[Site] = Site.objects.filter(user=request.user)
    return render(request, "password_manager/site_list.html", {"sites": sites, "form": form})