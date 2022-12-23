from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('username', 'password', 'first_name', 'last_name')}),
    ('Permissions', {'fields': (
      'is_active', 
      'is_staff', 
      'is_superuser',
      'groups', 
      'user_permissions',
    )}),
  )
  add_fieldsets = (
    (
      None,
      {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2')
      }
    ),
  )

  list_display = ('username', 'first_name', 'last_name', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('username',)
  ordering = ('username',)
  filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)

