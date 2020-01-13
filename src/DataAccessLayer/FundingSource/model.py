from django.db import models
from ..BaseModel import BaseModel

class FundingSource(BaseModel):
    userId = models.UUIDField(editable=False)
    fundingSourceTypeId = models.UUIDField(editable=False)
    sourceNumber = models.CharField()
    issuerId = models.UUIDField(editable=False)
