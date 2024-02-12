from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import site_list, add_site, edit_site, delete_site, user_login, user_signup, user_logout, export_csv

urlpatterns = [
    path("", site_list, name="site_list"),
    path("add/", add_site, name="add_site"),
    path("edit/<int:pk>/", edit_site, name="edit_site"),
    path("delete/<int:pk>/", delete_site, name="delete_site"),
    path("export/", export_csv, name="export"),
    path("accounts/login/", user_login, name="login"),
    path("accounts/signup/", user_signup, name="signup"),
    path("accounts/logout/", user_logout, name="logout"),
]

"""
URL patterns for the password_manager app.

Includes the following paths:
- "" (empty path): site_list view
- "add/": add_site view
- "edit/<int:pk>/": edit_site view
- "delete/<int:pk>/": delete_site view
- "accounts/login/": user_login view
- "accounts/signup/": user_signup view
- "accounts/logout/": user_logout view
"""