from django.db import models


class UserBD(models.Model):
    roleId = models.CharField(max_length=100)
    login = models.TextField(null=True, blank=True)
    displayName = models.TextField(null=True, blank=True)
    pictureId = models.IntegerField()
    phoneNumber = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)