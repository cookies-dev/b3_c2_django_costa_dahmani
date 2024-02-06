from multiprocessing.managers import BaseManager

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Site
from .forms import SiteForm


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