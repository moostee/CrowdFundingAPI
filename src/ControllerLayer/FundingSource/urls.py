from django.urls import path
from ControllerLayer.FundingSource.views import FundingSourceForUser

urlpatterns = [
    path('v1/get_all/<uuid:userId>', FundingSourceForUser.as_view()),
]
