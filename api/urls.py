from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.common.v1.urls')),
    path('driver/', include('api.driver.driver_auth.urls')),
    path('client/', include('api.client.v1.urls'))
]
