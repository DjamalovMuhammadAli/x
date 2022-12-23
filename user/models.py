from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
  name = models.CharField(max_length=100)
  identifier = models.CharField(max_length=40, unique=True)
  USERNAME_FIELD = 'indentifier'

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
