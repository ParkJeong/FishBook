from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'userId',
            'userPw',
            'name',
            'email',
            'rrn',
            'last_destination',
            'created_at',
            'updated_at',
    )
    search_fields = (
            'userId',
            'name',
    )
# Register your models here.
