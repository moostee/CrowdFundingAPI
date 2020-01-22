from django.urls import path
from ControllerLayer.Issuer.viewsets import Issuer

urlpatterns = [
    path('v1', Issuer.as_view()),
]
