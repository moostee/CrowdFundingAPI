from django.urls import path
from ControllerLayer.FundingGroupType.viewsets import FundingGroupTypeList, FundingGroupTypeDetail
from django.urls import path
from ControllerLayer.FundingGroupType.viewsets import FundingGroupTypeList, FundingGroupTypeDetail

urlpatterns = [
    path('v1/', FundingGroupTypeList.as_view()),
    path('v1/<uuid:pk>', FundingGroupTypeDetail.as_view()),
]
