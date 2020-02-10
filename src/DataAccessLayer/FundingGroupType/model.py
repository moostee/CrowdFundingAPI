from django.db import models
from ..BaseModel import BaseModel
from django.contrib.postgres.fields import JSONField

class FundingGroupType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    hasFixedIndividualAmount = models.BooleanField()
    hasFixedGroupAmount = models.BooleanField()
    hasMaturityDate = models.BooleanField()
    maxUser = models.PositiveSmallIntegerField()
    minUser = models.PositiveSmallIntegerField()
    isAutomatedCycle = models.BooleanField()
    defaultCycleDuration = models.CharField(max_length=10)
    hasRollingBeneficiary = models.BooleanField()
    hasFixedDefaultCycle = models.BooleanField()
    canJoinClosedGroup = models.BooleanField()
    description = models.CharField(max_length=256)
    config = JSONField()
