# Third party
from uuid import uuid4

# Djando core models
from django.db import models


class BaseModel(models.Model):
    """Project Base model.

    Abstract model to inherit to other models in the project
    Fields:

    - id: uuid field
    - created_at: DateTime field
    - updated_at: DateTime field
    - status: Char field
    """

    STATUS = (
        ('ACTIVE', 'Active'),
        ('DEACTIVATED', 'Deactivated'),
        ('DONE', 'Done')
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    status = models.CharField(
        "Status",
        max_length=35,
        choices=STATUS,
        null=False,
        blank=False
    )

    class Meta:
        abstract = True
