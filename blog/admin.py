# Register your models here.
from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'created_at', 'updated_at', 'view_counter']
    list_filter = ['is_published', 'created_at', "view_counter"]
