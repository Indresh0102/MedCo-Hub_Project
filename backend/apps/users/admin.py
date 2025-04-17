from django.contrib import admin
from .models import CustomUser
# Register your models here.

class usersAdmin(admin.ModelAdmin):
    list_display = []

admin.site.register(CustomUser, usersAdmin)