from django.db import models
from django.contrib.postgres.fields import JSONField

# Utils
from utils.base_model import BaseModel


class Survey(BaseModel):
    updated_at = None
    status = None

    activity = models.OneToOneField(
        'activity.Activity',
        on_delete=models.CASCADE
    )
    answers = JSONField(default={})

    def __str__(self):
        """Str representation."""
        return f'{self.activity}'
