from ..BaseModel import BaseModel
from django.db import models

class Funding(BaseModel):
        fundingGroupId = models.ForeignKey()
        beneficiaryId = models.ForeignKey()
        cycle = models.IntegerField()
        amount = models.DecimalField(max_digits=19,decimal_places=2)
        currency = models.CharField(max_length=50)
        dueDate = models.DateField(blank=True)

