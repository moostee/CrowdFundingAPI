from django.urls import path
from ControllerLayer.Issuer.viewsets import Issuer, IssuerDetails

urlpatterns = [
    path('v1', Issuer.as_view()),
    path('v1/<uuid:pk>', IssuerDetails.as_view()),
]
