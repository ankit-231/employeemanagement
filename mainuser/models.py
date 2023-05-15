from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'))
    role = models.CharField(_('role'), max_length=250)
    is_deleted = models.BooleanField("isdeleted", default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

    def __str__(self):
        return self.username