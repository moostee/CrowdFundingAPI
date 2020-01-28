from django.db import models
from ..BaseModel import BaseModel
from ..FundingSourceType.model import FundingSourceType
from ..Issuer.model import Issuer
from ..User.model import User
class FundingSource(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fundingSourceType = models.ForeignKey(FundingSourceType, on_delete=models.CASCADE)
    sourceNumber = models.CharField(max_length=20)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
