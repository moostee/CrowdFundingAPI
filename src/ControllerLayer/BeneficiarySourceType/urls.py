from django.urls import path
from ControllerLayer.BeneficiarySourceType.views import BeneficiarySourceTypeList,BeneficiarySourceTypeDetail

urlpatterns = [
    path('v1', BeneficiarySourceTypeList.as_view()),
    path('v1/<uuid:pk>', BeneficiarySourceTypeDetail.as_view()),
]
