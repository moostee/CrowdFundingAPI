from django.urls import path
from ControllerLayer.User.viewsets import UserLogin, UserSignup

urlpatterns = [
    path('v1/signin', UserLogin.as_view()),
    path('v1/signup', UserSignup.as_view())
]
