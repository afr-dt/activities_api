from django.contrib import admin

# Model
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = [
        'property',
        'schedule',
        'title',
        'created_at',
        'updated_at',
        'status'
    ]
    list_display = [
        'property',
        'schedule',
        'title',
        'created_at',
        'updated_at',
        'status'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
