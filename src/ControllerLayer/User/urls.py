from django.urls import path
from ControllerLayer.User.viewsets import UserSignup

urlpatterns = [
    path('v1/signup', UserSignup.as_view())
]
