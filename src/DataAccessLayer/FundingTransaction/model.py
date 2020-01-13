from django.db import models
from django.utils.translation import ugettext as _
import uuid

from ..BaseModel import BaseModel


class FundingTransaction(BaseModel):

    PENDING = "pending"
    SUCCESSFUL = "successful"
    FAILED = "failed"

    STATUS = [
        (PENDING, _('pending transaction')),
        (SUCCESSFUL, _('successful transaction')),
        (FAILED, _('failed transaction')),
    ]

    userId = models.UUIDField(editable=False)
    fundingId = models.ForeignKey(FundingGroup, on_delete=models.CASCADE)
    fundingSourceId = models.ForeignKey(
        FundingSource, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=100)
    paymentTransactionRef = models.CharField(max_length=255)
    issuerId = models.ForeignKey(Issue, on_delete=models.CASCADE)
    status = models.CharField(
        default=PENDING,
        choices=STATUS,
        max_length=100
    )
    issuerResponseCode = models.CharField(max_length=100)
    issuerPaymentReference = models.CharField(max_length=100)
    issuerRemark = models.CharField(max_length=255)
