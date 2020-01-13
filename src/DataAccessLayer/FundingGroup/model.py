from django.db import models
from ..BaseModel import BaseModel
from django.utils.translation import ugettext as _
import uuid
from ..FundingGroupType.model import FundingGroupType
from ..User.model import User
class FundingGroup(BaseModel):
    CONTINUE = "Continue"
    ABORT = "Abort"
    HOLD = "Hold"

    FAILUREACTION = [
        (CONTINUE, _('Continue Process')),
        (ABORT, _('Abort Process')),
        (HOLD, _('Hold Process')),
    ]

    name = models.CharField(max_length=100)
    fundingGroupTypeId = models.ForeignKey(FundingGroupType, on_delete=models.CASCADE)
    totalCycles = models.IntegerField()
    currentCycle = models.IntegerField()
    initiatorId = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    nextCycleDate = models.DateTimeField()
    cycleDuration = models.CharField(max_length=10)
    code = models.CharField(max_length=50)
    isClosed = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2,max_digits=19)
    currency = models.CharField(max_length=10)
    targetGroupAmount = models.DecimalField(decimal_places=2,max_digits=19)
    targetGroupDate = models.DateTimeField()
    debitBeneficiary = models.BooleanField(default=False)
    failureAction = models.CharField(
        max_length=64,
        choices=FAILUREACTION,
    )
    description = models.CharField(max_length=256)
