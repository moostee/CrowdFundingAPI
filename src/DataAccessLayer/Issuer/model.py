from ..BaseModel import BaseModel
from django.db import models

class Issuer(BaseModel):
    name = models.CharField(max_length=100)
    referenceType = models.CharField(max_length=50)
    referenceTypeMaxChar = models.IntegerField()
    