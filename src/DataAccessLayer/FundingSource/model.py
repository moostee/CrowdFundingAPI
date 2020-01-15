from django.db import models
from ..BaseModel import BaseModel
from ..FundingSourceType.model import FundingSourceType
from ..Issuer.model import Issuer
from ..User.model import User
class FundingSource(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    fundingSourceTypeId = models.ForeignKey(FundingSourceType, on_delete=models.CASCADE)
    sourceNumber = models.CharField(max_length=20)
    issuerId = models.ForeignKey(Issuer, on_delete=models.CASCADE)
