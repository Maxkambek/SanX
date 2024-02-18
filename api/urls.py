from django.urls import path, include
from api.common.v1.views import VersionProjectListAPIView

urlpatterns = [
    path('auth/', include('api.common.v1.urls')),
    path('driver/', include('api.driver.driver_auth.urls')),
    path('driver-driver_main/', include('api.driver.driver_tools.urls')),
    path('client/', include('api.client.v1.urls')),
    path('versions/', VersionProjectListAPIView.as_view()),
    path('logistic/', include('api.logistic.api.urls'))
]
