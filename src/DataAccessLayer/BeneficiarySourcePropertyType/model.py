from django.db import models
from ..BaseModel import BaseModel
from django.utils.translation import ugettext as _
from ..BeneficiarySourceType.model import BeneficiarySourceType

class BeneficiarySourcePropertyType(BaseModel):
    beneficiarySourceTypeId = models.ForeignKey(BeneficiarySourceType, on_delete=models.CASCADE)
    name = models.CharField(default=False, max_length=50)
    dataType = models.CharField(max_length=64)
