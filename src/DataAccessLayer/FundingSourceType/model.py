from ..BaseModel import BaseModel
from django.db import models

class FundingSourceType(BaseModel):
        name = models.CharField(max_length=100)
        