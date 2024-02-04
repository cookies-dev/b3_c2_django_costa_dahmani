from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import site_list, add_site, edit_site, delete_site, user_login, user_signup, user_logout

urlpatterns = [
    path("", site_list, name="site_list"),
]
