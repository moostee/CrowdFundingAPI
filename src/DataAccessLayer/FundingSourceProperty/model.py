from django.db import models
from ..BaseModel import BaseModel
from ..FundingSourceType.model import FundingSourceType
from ..FundingSourcePropertyType.model import FundingSourcePropertyType

class FundingSourceProperty(BaseModel):
    fundingSourceTypeId = models.ForeignKey(FundingSourceType, on_delete=models.CASCADE)
    fundingSourcePropertyTypeId = models.ForeignKey(FundingSourcePropertyType, on_delete=models.CASCADE)
    propertyValue = models.CharField(null=False, max_length=100)
