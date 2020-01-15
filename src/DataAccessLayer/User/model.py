from django.db import models
from ..BaseModel import BaseModel

class User(BaseModel):
    userId = models.UUIDField(editable=False)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
