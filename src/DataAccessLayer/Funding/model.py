from ..BaseModel import BaseModel
from django.db import models
from ..FundingGroup.model import FundingGroup
from ..BeneficiarySource.model import BeneficiarySource
from ..User.model import User
class Funding(BaseModel):
        fundingGroupId = models.ForeignKey(FundingGroup, on_delete=models.CASCADE)
        beneficiaryId = models.ForeignKey(User, on_delete=models.CASCADE)
        cycle = models.IntegerField()
        amount = models.DecimalField(max_digits=19,decimal_places=2)
        currency = models.CharField(max_length=50)
        dueDate = models.DateField(blank=True)
