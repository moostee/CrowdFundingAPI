from django.db import models
from ..BaseModel import BaseModel

class User(BaseModel):
    userId = models.CharField(max_length=100)
    firstNname = models.CharField(max_length=100)
    lastNname = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
