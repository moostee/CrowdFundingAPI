from django.db import models
from ..BaseModel import BaseModel
from django.utils.translation import ugettext as _
from ..FundingSourceType.model import FundingSourceType

class FundingSourcePropertyType(BaseModel):
    fundingSourceTypeId = models.ForeignKey(FundingSourceType, on_delete=models.CASCADE)
    name = models.CharField(default=False, max_length=50)
    dataType = models.CharField(max_length=64)
