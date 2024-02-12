from multiprocessing.managers import BaseManager

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpRequest, HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Site
from .forms import SiteForm, LoginForm

import csv


@login_required
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


@login_required
def add_site(request: HttpRequest) -> JsonResponse:
    """
    Add a new site to the password manager.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the success or failure of the operation.
    """
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
    return redirect("site_list")


@login_required
def edit_site(request: HttpRequest, pk: int) -> HttpResponse:
    """
    View function that handles the editing of a site for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the site to be edited.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML template.
    """
    site: BaseManager[Site] = Site.objects.get(pk=pk)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
    return redirect("site_list")


@login_required
def delete_site(request: HttpRequest, pk: int) -> HttpResponse:
    """
    View function that handles the deletion of a site for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the site to be deleted.

    Returns:
        HttpResponse: The HTTP response object redirecting to the site list.
    """
    site = Site.objects.get(pk=pk)
    site.delete()
    return redirect("site_list")


def user_signup(request: HttpRequest):
    """
    View function that handles the user signup process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML template.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "password_manager/signup.html", {"form": form})


def user_login(request: HttpRequest):
    """
    View function that handles the user login process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML template.
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("site_list")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "password_manager/login.html", {"form": form})


def user_logout(request: HttpRequest):
    """
    View function that handles the user logout process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object redirecting to the login page.
    """
    logout(request)
    return redirect("login")


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def export_csv(request: HttpRequest):

    queryset = Site.objects.all()

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow([field for field in row]) for row in queryset.values_list()),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="export.csv"'},
    )
