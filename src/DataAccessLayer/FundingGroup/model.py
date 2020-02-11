from django.db import models
from ..BaseModel import BaseModel
from django.utils.translation import ugettext as _
import uuid
from ..FundingGroupType.model import FundingGroupType
from ..User.model import User
class FundingGroup(BaseModel):
    CONTINUE = "continue"
    ABORT = "abort"
    HOLD = "hold"

    FAILUREACTION = [
        (CONTINUE, _('Continue Process')),
        (ABORT, _('Abort Process')),
        (HOLD, _('Hold Process')),
    ]

    name = models.CharField(max_length=100)
    fundingGroupType = models.ForeignKey(FundingGroupType, related_name='fundingGroupType', on_delete=models.CASCADE, null=False)
    totalCycles = models.PositiveSmallIntegerField(default=1)
    currentCycle = models.PositiveSmallIntegerField(default=1)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateField()
    nextCycleDate = models.DateField(null=True)
    cycleDuration = models.CharField(max_length=10, null=True)
    code = models.CharField(max_length=13, unique=True)
    isClosed = models.BooleanField(default=False)
    individualAmount = models.DecimalField(decimal_places=2, max_digits=19, null=True)
    currency = models.CharField(max_length=10, null=True)
    targetGroupAmount = models.DecimalField(decimal_places=2, max_digits=19, null=True)
    targetGroupDate = models.DateField(null=True)
    debitBeneficiary = models.BooleanField(default=False)
    failureAction = models.CharField(
        max_length=64,
        choices=FAILUREACTION,
    )
    description = models.CharField(max_length=256)
