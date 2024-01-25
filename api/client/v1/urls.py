from django.urls import path
from . import views

urlpatterns = [
    path('full-name/', views.ClientFullNameCreateAPIView.as_view()),
    path('full-name-update-retrieve/', views.ClientFullNameRetrieveUpdateAPIView.as_view()),
    path('avatar/', views.ClientAvatarCreateAPIView.as_view()),
    path('avatar-retrieve-update/', views.ClientAvatarRetrieveUpdateAPIView.as_view()),
    path('date-birth/', views.ClientDateBirthCreateAPIView.as_view()),
    path('date-birth-retrieve-update/', views.ClientDateBirthRetrieveUpdateAPIView.as_view()),
    path('order-create/', views.OrderCreateAPIView.as_view()),
    path('order-list/', views.OrderListAPIView.as_view()),
    path('order/<int:pk>/', views.OrderDetailAPIView.as_view())

]
