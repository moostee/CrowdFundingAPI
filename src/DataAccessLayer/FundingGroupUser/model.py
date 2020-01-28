from django.db import models
import uuid
from django.utils.translation import ugettext as _
from ..BaseModel import BaseModel
from ..FundingGroup.model import FundingGroup
from ..BeneficiarySource.model import BeneficiarySource
from ..FundingSource.model import FundingSource
from ..Role.model import Role
from ..User.model import User

class FundingGroupUser(BaseModel):
    PENDING = "Pending"
    APPROVED = "Approved"
    DECLINED = "Declined"

    USERSTATUS = [
        (PENDING, _('User approval pending')),
        (APPROVED, _('User Approved')),
        (DECLINED, _('User declined')),
    ]

    beneficiarySource = models.ForeignKey(BeneficiarySource, on_delete=models.CASCADE)
    fundingSource = models.ForeignKey(FundingSource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fundingGroup = models.ForeignKey(FundingGroup, on_delete=models.CASCADE)
    userSequence = models.PositiveSmallIntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2,max_digits=19)
    status = models.CharField(
        max_length=64,
        choices=USERSTATUS,
    )
