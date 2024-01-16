from django.urls import path
from . import views

urlpatterns = [
    path('country-list/', views.CountryListAPIView.as_view(), name='country-list'),
    path('direction-list/', views.LocationListAPIView.as_view(), name='direction-list'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('verify-register/', views.CheckVerifyCodeAPIView.as_view(), name='verify-register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('verify-login/', views.LoginVerifyAPIView.as_view(), name='verify-login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout')
]
