from django.db import models
import uuid
from django.utils import timezone

class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta :
        abstract = True
