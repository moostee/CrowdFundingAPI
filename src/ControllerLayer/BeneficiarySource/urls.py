from django.urls import path
from ControllerLayer.BeneficiarySource.views import BeneficiarySourceForUserList

urlpatterns = [
    path('v1', BeneficiarySourceForUserList.as_view()),
]