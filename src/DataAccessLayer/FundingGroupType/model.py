from django.db import models
from ..BaseModel import BaseModel

class FundingGroupType(BaseModel):
    name = models.CharField(max_length=100)
    hasFixedIndividualAmount = models.BooleanField(default=False)
    hasFixedGroupAmount = models.BooleanField(default=False)
    hasMaturityDate = models.BooleanField(default=False)
    maxUser = models.IntegerField()
    minUser = models.IntegerField()
    isAutomatedCycle = models.BooleanField(default=False)
    defaultCycleDuration = models.CharField(max_length=10)
    hasRollingBeneficiary = models.BooleanField(default=False)
    hasFixedDefaultCycle = models.BooleanField(default=False)
    canJoinClosedGroup = models.BooleanField(default=False)
