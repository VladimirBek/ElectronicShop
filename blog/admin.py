from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'view_count',)
    list_filter = ('published',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {"slug": ("title",)}
