from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'species',
        'description',
        'image',
        'view_count',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'species',
    )
# Register your models here.
