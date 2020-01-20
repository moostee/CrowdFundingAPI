from django.db import models
from ..BaseModel import BaseModel
from ..FundingSource.model import FundingSource
from ..FundingSourcePropertyType.model import FundingSourcePropertyType

class FundingSourceProperty(BaseModel):
    fundingSourceId = models.ForeignKey(FundingSource, on_delete=models.CASCADE)
    fundingSourcePropertyTypeId = models.ForeignKey(FundingSourcePropertyType, on_delete=models.CASCADE)
    propertyValue = models.CharField(null=False, max_length=100)
