from ..BaseModel import BaseModel
from django.db import models
from django.contrib.postgres.fields import JSONField

class FundingSourceType(BaseModel):
        name = models.CharField(max_length=100, unique=True)
        config = JSONField()
        