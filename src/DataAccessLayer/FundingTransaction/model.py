from django.db import models
from django.utils.translation import ugettext as _
import uuid
from ..BaseModel import BaseModel
from ..Funding.model import Funding
from ..FundingSource.model import FundingSource
from ..Issuer.model import Issuer
from ..User.model import User

class FundingTransaction(BaseModel):

    PENDING = "pending"
    SUCCESSFUL = "successful"
    FAILED = "failed"

    STATUS = [
        (PENDING, _('pending transaction')),
        (SUCCESSFUL, _('successful transaction')),
        (FAILED, _('failed transaction')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    funding = models.ForeignKey(Funding, on_delete=models.CASCADE)
    fundingSource = models.ForeignKey(FundingSource, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=100)
    paymentTransactionRef = models.CharField(max_length=255)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    status = models.CharField(
        default=PENDING,
        choices=STATUS,
        max_length=100
    )
    issuerResponseCode = models.CharField(max_length=100)
    issuerPaymentReference = models.CharField(max_length=100)
    issuerRemark = models.CharField(max_length=255)
