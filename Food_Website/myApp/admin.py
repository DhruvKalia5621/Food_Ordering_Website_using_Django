from django.contrib import admin
from.models import *
from django.contrib.auth.models import User
from .models import Profile2
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile2

# Extend the UserAdmin to include the profile inline
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Member)
admin.site.register(profile)
admin.site.register(Complaints)
admin.site.register(CustomerOrders)
