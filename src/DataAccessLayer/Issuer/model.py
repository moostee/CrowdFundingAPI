from ..BaseModel import BaseModel
from django.db import models
from django.utils.translation import ugettext as _

class Issuer(BaseModel):
    ALPHA_NUMERIC = "alpha-numeric"
    NUMERIC = "numeric"
    ALPHA = "alpha"

    REFERENCETYPES = [
        (ALPHA_NUMERIC, _('Containing alphabets and numbers')),
        (NUMERIC, _('Containing only numbers')),
        (ALPHA, _('Containing only alphabets')),
    ]

    name = models.CharField(max_length=100, unique=True)
    referenceTypeMaxChar = models.PositiveSmallIntegerField()
    referenceType =  models.CharField(
        max_length=32,
        choices=REFERENCETYPES,
    )
    