from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib import auth
# from django import apps
from django.apps import apps


class CustomUserManager(UserManager):
  use_in_migrations = True

  def _create_user(self, email, password, first_name, last_name, username, phone_number, **extra_fields):

    if not username:
      raise ValueError("The given username must be set")
    email = self.normalize_email(email)
    if not password:
      raise ValueError('Password is not provided')
    # Lookup the real model class from the global app registry so this
    # manager method can be used in migrations. This is fine because
    # managers are by definition working on the real model.
    GlobalUserModel = apps.get_model(
      self.model._meta.app_label, self.model._meta.object_name
    )
    user = self.model(
      username = username,
      email = self.normalize_email(email),
      first_name = first_name,
      last_name = last_name,
      phone_number = phone_number,
      **extra_fields
    )
    username = GlobalUserModel.normalize_username(username)
    user = self.model(username=username, email=email, **extra_fields)
    user.password = make_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, first_name=None, last_name=None, username=None, phone_number=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault('is_active', True)
    extra_fields.setdefault("is_superuser", False)
    return self._create_user(email, password, first_name, last_name, username, phone_number, **extra_fields)

  def create_superuser(self, email, password, first_name, last_name, username, phone_number, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault('is_active', True)
    extra_fields.setdefault("is_superuser", True)

    if extra_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get("is_superuser") is not True:
      raise ValueError("Superuser must have is_superuser=True.")

    return self._create_user(email, password, first_name, last_name, username, phone_number, **extra_fields)

  def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
    if backend is None:
      backends = auth._get_backends(return_tuples=True)
      if len(backends) == 1:
        backend, _ = backends[0]
      else:
        raise ValueError(
          "You have multiple authentication backends configured and "
          "therefore must provide the `backend` argument."
        )
    elif not isinstance(backend, str):
      raise TypeError(
        "backend must be a dotted import path string (got %r)." % backend
      )
    else:
      backend = auth.load_backend(backend)
    if hasattr(backend, "with_perm"):
      return backend.with_perm(
        perm,
        is_active=is_active,
        include_superusers=include_superusers,
        obj=obj,
      )
    return self.none()


class User(AbstractBaseUser, PermissionsMixin):
  avatar = models.ImageField(upload_to='user_avatar/', null=True, blank=True)
  first_name = models.CharField(max_length=255, null=True, blank=True)
  last_name = models.CharField(max_length=255, null=True, blank=True)
  email = models.EmailField(db_index=True, unique=True, max_length=254)
  username = models.CharField(max_length=255, unique=True)
  is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
  is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
  is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.
  last_login = models.DateTimeField(null=True, blank=True)
  date_joined = models.DateTimeField(default = timezone.now)
  phone_number = models.CharField(max_length=13, unique=True)
  # sms_code = models.CharField('СМС код', default='', max_length=9)
  # temp = models.CharField('Temprorary', default='', max_length=200)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone_number']

  @property
  def is_authenticated(self):
    return True

  def __str__(self):
    return self.username

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'

