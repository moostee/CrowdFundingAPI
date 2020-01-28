from django.urls import path
from ControllerLayer.Funding.viewsets import FundingList
from django.urls import path

urlpatterns = [
    path('v1', FundingList.as_view()),
]
