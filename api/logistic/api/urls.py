from . import views
from django.urls import path

urlpatterns = [
    path('companies/', views.LogisticCompanyListAPIView.as_view()),
    path('companies/<int:pk>/', views.LogisticCompanyDetailAPIView.as_view()),
    path('orders/', views.OrderListAPIViewForLogistic.as_view()),
    path('orders/<int:pk>/', views.OrderDetailAPIViewForLogistic.as_view()),
    path('drivers/', views.DriverListAPIView.as_view()),
    path('drivers/<int:pk>/', views.DriverDetailAPIView.as_view()),
    path('my-drivers/', views.MyDriversListAPIView.as_view())
]
