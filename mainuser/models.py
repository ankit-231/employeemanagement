from django.db import models
from django.utils import timezone

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'))
    is_deleted = models.BooleanField("isdeleted", default=0)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# my models

import uuid

class Role(models.Model):
    name = models.CharField(max_length=250, unique=True)
    is_deleted = models.BooleanField(default=False)
    user_role = models.ManyToManyField(CustomUser())

class DesignationHead(models.Model):
    name = models.CharField(max_length=250, unique=True)
    is_deleted = models.BooleanField(default=False)
    

class Designation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False)
    designation_head = models.ForeignKey(DesignationHead(), on_delete=models.SET_NULL, null=True, blank=True)
