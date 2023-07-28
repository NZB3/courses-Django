from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Name', max_length=30, null=True)
    photo = models.ImageField(verbose_name="Photo", upload_to='users/photos', blank=True, null=True)
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)

    is_active = models.BooleanField(verbose_name='active', default=False)
    is_staff = models.BooleanField(verbose_name='creator', default=False)
    is_superuser = models.BooleanField(verbose_name='admin', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

