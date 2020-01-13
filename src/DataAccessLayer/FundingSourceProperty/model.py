from django.db import models
from ..BaseModel import BaseModel

class FundingSourceProperty(BaseModel):
    fundingSourceTypeId = models.UUIDField(editable=False)
    fundingSourcePropertyTypeId = models.UUIDField(editable=False)
    propertyValue = models.CharField(null=False)
