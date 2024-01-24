from django.urls import path
from . import views

urlpatterns = [
    path('full-name/', views.ClientFullNameCreateAPIView.as_view()),
    path('full-name-update-retrieve/', views.ClientFullNameRetrieveUpdateAPIView.as_view()),
    path('avatar/', views.ClientAvatarRetrieveUpdateAPIView.as_view()),
    path('avatar-retrieve-update/', views.ClientAvatarRetrieveUpdateAPIView.as_view()),
    path('date-birth/', views.ClientDateBirthCreateAPIView.as_view()),
    path('date-birth-retrieve-update/', views.ClientDateBirthRetrieveUpdateAPIView.as_view())
]
