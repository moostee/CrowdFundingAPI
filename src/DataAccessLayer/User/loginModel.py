from django.db import models
from ..BaseModel import BaseModel


class LoginModel(BaseModel):
    userId = models.UUIDField(editable=False)
    phoneNumber = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=6, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
