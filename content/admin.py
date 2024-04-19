from django.contrib import admin
from .models import Page
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin):
    search_fields = ("name__startswith",)
    list_display = ("tree_actions", "indented_title", "name", "url", "active",)
    list_filter = ("active",)
    list_display = ("indeted_title",)
    prepopulated_fields = {"url": ("name",)}