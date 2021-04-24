from django.db import models

# Utils
from utils.base_model import BaseModel


class Activity(BaseModel):
    property = models.ForeignKey(
        'property.Property',
        on_delete=models.CASCADE
    )
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
