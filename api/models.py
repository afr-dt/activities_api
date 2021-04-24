from django.db import models
from django.contrib.postgres.fields import JSONField

# Utils
from .utils.base_model import BaseModel


class Property(BaseModel):
    title = models.CharField(
        "Title",
        max_length=255,
        null=False,
        blank=False
    )
    address = models.TextField(
        "Address",
        null=False,
        blank=False
    )
    description = models.TextField(
        "Description",
        null=False,
        blank=False
    )
    disabled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """Str representation."""
        return f'{self.title}'


class Activity(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    schedule = models.DateTimeField(
        "Schedule",
        auto_now=False,
        auto_now_add=False
    )
    title = models.CharField(
        "Title",
        max_length=255,
        null=False,
        blank=True
    )

    def __str__(self):
        """Str representation."""
        return f'{self.title}'


class Survey(BaseModel):
    updated_at = None
    status = None

    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    answers = JSONField(default={})

    def __str__(self):
        """Str representation."""
        return f'{self.activity}'
