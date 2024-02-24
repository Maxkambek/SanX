from . import views
from django.urls import path

urlpatterns = [
    path('wish-list/', views.WishlistListAPIView.as_view()),
    path('add-to-wishlist/', views.AddToWishlistAPIView.as_view()),
    path('delete-from-wishlist/<int:pk>/', views.DeleteFromWishlistAPIView.as_view()),
    path('drivers-locations/', views.DriverCurrentLocationAPIView.as_view()),
    path('change-location/', views.DriverCurrentLocationChangeAPIView.as_view())
]
