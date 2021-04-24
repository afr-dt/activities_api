from django.contrib import admin

# Model
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'address',
        'description',
        'created_at',
        'updated_at',
        'disabled_at',
        'status'
    ]
    list_display = [
        'title',
        'address',
        'description',
        'created_at',
        'updated_at',
        'disabled_at',
        'status'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'disabled_at',
    ]
