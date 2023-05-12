from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
        None, 
        {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }
        )
    )

# Register your models here.


