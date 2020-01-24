from django.db import models
from ..BaseModel import BaseModel
from ..BeneficiarySourceType.model import BeneficiarySourceType

class BeneficiarySourceProperty(BaseModel):
    beneficiarySourceTypeId = models.ForeignKey(BeneficiarySourceType, on_delete=models.CASCADE)
    propertyType = models.CharField(default=False,max_length=100)
    propertyValue = models.CharField(null=False, max_length=100)
