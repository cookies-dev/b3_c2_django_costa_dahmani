from django.db import models
from django.contrib.auth.models import User

class Meta:
    app_label = 'password_manager'

class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __doc__(self):
        """
        Represents a website or online service.

        Attributes:
            user (User): The user associated with the site.
            name (str): The name of the site.
            url (str): The URL of the site.
            username (str): The username for the site.
            password (str): The password for the site.

        Returns:
            str: The name of the site.
        """
