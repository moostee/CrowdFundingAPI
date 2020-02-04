from django.urls import path
from ControllerLayer.BeneficiarySource.views import BeneficiarySourceForUserList, BeneficiarySourceForUserDetails

urlpatterns = [
    path('v1', BeneficiarySourceForUserList.as_view()),
    path('v1/<uuid:beneficiarySourceId>', BeneficiarySourceForUserDetails.as_view()),
]