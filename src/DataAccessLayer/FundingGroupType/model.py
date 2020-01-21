from django.db import models
from ..BaseModel import BaseModel

class FundingGroupType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    hasFixedIndividualAmount = models.BooleanField()
    hasFixedGroupAmount = models.BooleanField()
    hasMaturityDate = models.BooleanField()
    maxUser = models.IntegerField()
    minUser = models.IntegerField()
    isAutomatedCycle = models.BooleanField()
    defaultCycleDuration = models.CharField(max_length=10)
    hasRollingBeneficiary = models.BooleanField()
    hasFixedDefaultCycle = models.BooleanField()
    canJoinClosedGroup = models.BooleanField()
    description = models.CharField(max_length=256)
