from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    roleId = models.CharField(max_length=100)
    login = models.TextField(null=True, blank=True)
    displayName = models.TextField(null=True, blank=True)
    pictureId = models.IntegerField(null=True, blank=True, default=00000)
    phoneNumber = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)


class Abonent(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    displayName = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pictureId = models.IntegerField(null=True, blank=True, default=00000)
    perimeterId = models.IntegerField(null=True, blank=True, default=00000)
    is_admin = models.BooleanField(default=False, help_text='Designates that this user has all permissions without '
                                                            'explicitly assigning them.', verbose_name='admin')
    pacsCode = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=30)
    floor = models.CharField(max_length=15)
    room = models.CharField(max_length=30)
    cars = models.CharField(max_length=30)
    isRegistered = models.BooleanField(default=False)
    modified = models.TextField(null=True, blank=True)