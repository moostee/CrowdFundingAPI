from django.db import models
from ..BaseModel import BaseModel
from ..BeneficiarySourceType.model import BeneficiarySourceType
from ..User.model import User

class BeneficiarySource(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiarySourceTypeId = models.ForeignKey(BeneficiarySourceType, on_delete=models.CASCADE)
    destinationNumber = models.CharField(max_length=20)
    issuerId = models.UUIDField(editable=False)
