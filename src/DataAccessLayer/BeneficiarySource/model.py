from django.db import models
from ..BaseModel import BaseModel
from ..BeneficiarySourceType.model import BeneficiarySourceType
from ..User.model import User

class BeneficiarySource(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiarySourceType = models.ForeignKey(BeneficiarySourceType, on_delete=models.CASCADE)
    destinationNumber = models.CharField(max_length=20)
    issuer = models.UUIDField(editable=False)
