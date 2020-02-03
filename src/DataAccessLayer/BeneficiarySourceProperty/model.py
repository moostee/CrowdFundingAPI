from django.db import models
from ..BaseModel import BaseModel
from ..BeneficiarySource.model import BeneficiarySource

class BeneficiarySourceProperty(BaseModel):
    beneficiarySource = models.ForeignKey(BeneficiarySource, on_delete=models.CASCADE)
    propertyType = models.CharField(default=False,max_length=100)
    propertyValue = models.CharField(null=False, max_length=100)
