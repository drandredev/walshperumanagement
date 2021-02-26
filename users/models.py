"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=255, blank=True)
    departamento = models.CharField(max_length=255, blank=True)
    celular = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
