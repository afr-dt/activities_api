from django.db import models

# Utils
from utils.base_model import BaseModel


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
