from django.db import models
from ..BaseModel import BaseModel
# import uuid

class FundingGroupType(BaseModel):
    name = models.CharField(max_length=100)
    hasFixedIndividualAmount = models.BooleanField(default=False)
    hasFixedGroupAmount = models.BooleanField(default=False)
    hasMaturityDate = models.BooleanField(default=False)
    maxUser = models.IntegerField()

