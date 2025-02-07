from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ControllerLayer.default.viewsets import DefaultViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="CrowdFunding API",
        default_version='v1',
        description="Python Django API Application For CrowdFunding",
        terms_of_service="https://www.ubagroup.com/uba-privacy-policy/",
        contact=openapi.Contact(email="ubainnovate@ubagroup.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', DefaultViewSet.as_view()),
    path('api/users/', include('ControllerLayer.User.urls')),
    path('api/fundinggrouptypes/', include('ControllerLayer.FundingGroupType.urls')),
    path('api/issuers/', include('ControllerLayer.Issuer.urls')),
    path('api/roles/', include('ControllerLayer.Role.urls')),
    path('api/beneficiarysourcetypes/', include('ControllerLayer.BeneficiarySourceType.urls')),
    path('api/fundings/', include('ControllerLayer.Funding.urls')),
    path('api/beneficiarysource/', include('ControllerLayer.BeneficiarySource.urls')), 
    path('api/fundingsourcetypes/', include('ControllerLayer.FundingSourceType.urls')),
    path('api/fundinggroups/', include('ControllerLayer.FundingGroup.urls')),
]
