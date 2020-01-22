from django.urls import path
from ControllerLayer.Role.viewsets import RoleList, RoleDetails

urlpatterns = [
    path('v1', RoleList.as_view()),
    path('v1/<uuid:pk>', RoleDetails.as_view())
]
