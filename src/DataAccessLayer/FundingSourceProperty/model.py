from django.db import models
from ..BaseModel import BaseModel
from ..FundingSource.model import FundingSource

class FundingSourceProperty(BaseModel):
    fundingSource = models.ForeignKey(FundingSource, on_delete=models.CASCADE)
    propertyName = models.CharField(null=False, max_length=100)
    propertyValue = models.CharField(null=False, max_length=100)
