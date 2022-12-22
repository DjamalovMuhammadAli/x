from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
  Name = models.CharField(_(""), max_length=50)
  identifier = models.CharField(max_length=40, unique=True)
  USERNAME_FIELD = 'indentifier'
