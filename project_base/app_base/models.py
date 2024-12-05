from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    SUPER_ADMIN = 'super_admin', 'Super Admin'
    ADMIN = 'admin', 'Admin'
    VIEWER = 'viewer', 'Viewer'


class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_super_admin(self):
        return self.role == Role.SUPER_ADMIN

    def is_admin(self):
        return self.role == Role.ADMIN

    def is_viewer(self):
        return self.role == Role.VIEWER
