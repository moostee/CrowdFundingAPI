from django.db import models
from ..BaseModel import BaseModel

class Role(BaseModel):
    name = models.CharField(max_length=100, unique=True)
