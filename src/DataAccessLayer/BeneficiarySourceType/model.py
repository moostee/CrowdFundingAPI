from ..BaseModel import BaseModel
from django.db import models

class BeneficiarySourceType(BaseModel):
        name = models.CharField(max_length=100)
        