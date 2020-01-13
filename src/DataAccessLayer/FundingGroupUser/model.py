from django.db import models
import uuid

from ..BaseModel import BaseModel


class FundingGroupUser(BaseModel):
    userId = models.UUIDField(editable=False)
    fundingGroupId = models.ForeignKey(FundingGroup, on_delete=models.CASCADE)
    userSequence = models.IntegerField()
    roleId = models.UUIDField(editable=False)
    balance = models.FloatField(default=0.0)
