from django.urls import path
from . import views

urlpatterns = [
    path('country-list/', views.CountryListAPIView.as_view(), name='country-list'),
    path('category-list/', views.CategoryList.as_view(), name='category-list'),
    path('district-list/<int:pk>/', views.DistrictListAPIView.as_view(), name='district-list'),
    path('direction-list/', views.LocationListAPIView.as_view(), name='direction-list'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('verify-register/', views.CheckVerifyCodeAPIView.as_view(), name='verify-register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('verify-login/', views.LoginVerifyAPIView.as_view(), name='verify-login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('faq/', views.FAQListAPIView.as_view()),
    path('news/', views.NewsListAPIView.as_view()),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view()),
    path('banners/', views.BannersListAPIView.as_view()),
    path('chat-create/', views.ChatCreateView.as_view()),
    path('chat-list/', views.ChatListView.as_view()),
    path('chat-list/<int:pk>/', views.ChatDetailView.as_view()),
    path('contract-create/', views.ContractsAPIView.as_view()),
    path('contract-list/', views.ContractListAPIView.as_view()),
]
