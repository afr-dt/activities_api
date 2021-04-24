from django.contrib import admin

# Model
from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    fields = [
        'activity',
        'answers',
        'created_at'
    ]
    list_display = [
        'activity',
        'answers',
        'created_at'
    ]
    readonly_fields = [
        'created_at'
    ]
