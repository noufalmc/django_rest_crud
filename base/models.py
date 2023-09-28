from django.db import models
import uuid

"""
    BASE USER MODEL
    This model not created tables in database, 
    This model class can extends for another classes.
"""


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        abstract = True

