from django.urls import path
from ControllerLayer.FundingSourceType.viewsets import FundingSourceTypeList, FundingSourceTypeDetail
from django.urls import path

urlpatterns = [
    path('v1', FundingSourceTypeList.as_view()),
    path('v1/<uuid:pk>', FundingSourceTypeDetail.as_view()),
]
