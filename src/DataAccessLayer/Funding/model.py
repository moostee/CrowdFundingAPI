from django.utils.translation import ugettext as _
from ..BaseModel import BaseModel
from django.db import models
from ..FundingGroup.model import FundingGroup
from ..BeneficiarySource.model import BeneficiarySource
from ..User.model import User
class Funding(BaseModel):
        PENDING = "pending"
        ACTIVE = "active"
        COMPLETED = "completed"

        STATUS = [
                (PENDING, _('Funding is pending')),
                (ACTIVE, _('Funding is active and yet to be paid')),
                (COMPLETED, _('Funding has been paid and is completed')),
        ]

        fundingGroup = models.ForeignKey(FundingGroup, related_name='fundingGroup', on_delete=models.CASCADE)
        beneficiary = models.ForeignKey(User, related_name='beneficiary', on_delete=models.CASCADE)
        cycle = models.PositiveSmallIntegerField()
        amount = models.DecimalField(max_digits=19,decimal_places=2)
        currency = models.CharField(max_length=50)
        dueDate = models.DateField(blank=True)
        status = models.CharField(
                default=PENDING,
                max_length=64,
                choices=STATUS,
    )
