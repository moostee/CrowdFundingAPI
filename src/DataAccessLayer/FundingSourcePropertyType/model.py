from django.db import models
from ..BaseModel import BaseModel
from django.utils.translation import ugettext as _

class FundingSourcePropertyType(BaseModel):
    fundingSourceTypeId = models.UUIDField(editable=False)
    name = models.CharField(default=False)
    dataType = models.CharField(max_length=64)
