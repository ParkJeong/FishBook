from django.contrib import admin


from .models import Admin

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'adminId',
            'adminPw',
            'name',
            'email',
            'bookmark',
            'created_at',
            'updated_at'
    )
    search_fields = (
            'adminId',
    )
# Register your models here.
