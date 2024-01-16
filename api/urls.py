from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.common.v1.urls')),
    path('auth/driver/', include('api.driver.driver_auth.urls'))
]
