from django.urls import path
from ControllerLayer.FundingGroup.viewsets import FundingGroup

urlpatterns = [
    path('v1', FundingGroup.as_view())
]
