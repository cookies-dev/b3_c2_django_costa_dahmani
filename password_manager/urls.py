from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import site_list, add_site, edit_site, delete_site, user_login, user_signup, user_logout

urlpatterns = [
    path("", site_list, name="site_list"),
    path("add/", add_site, name="add_site"),
    path("edit/<int:pk>/", edit_site, name="edit_site"),
    path("delete/<int:pk>/", delete_site, name="delete_site"),
    path("accounts/signup/", user_signup, name="signup"),
]
