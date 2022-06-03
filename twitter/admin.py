from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    filter_horizontal = ['follows']
    fieldsets = (
        (None, {"fields": ("image", "follows")}),
    )


class UserAdmin(AuthUserAdmin):
    model = User
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
    )
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
