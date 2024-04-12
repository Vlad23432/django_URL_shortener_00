from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    list_display = ("name", "url", "active",)
    list_filter = ("active",)