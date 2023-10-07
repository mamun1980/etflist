from django.contrib import admin
from .models import HashKey


@admin.register(HashKey)
class HashKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'hash']