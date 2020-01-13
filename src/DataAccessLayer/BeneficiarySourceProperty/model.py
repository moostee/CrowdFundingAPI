from django.db import models
from ..BaseModel import BaseModel
from ..BeneficiarySourceType.model import BeneficiarySourceType
from ..BeneficiarySourcePropertyType.model import BeneficiarySourcePropertyType

class BeneficiarySourceProperty(BaseModel):
    beneficiarySourceTypeId = models.ForeignKey(BeneficiarySourceType, on_delete=models.CASCADE)
    beneficiarySourcePropertyTypeId = models.ForeignKey(BeneficiarySourcePropertyType, on_delete=models.CASCADE)
    propertyValue = models.CharField(null=False, max_length=100)
