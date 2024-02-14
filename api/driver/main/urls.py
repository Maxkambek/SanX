from . import views
from django.urls import path

urlpatterns = [
    path('wish-list/', views.WishlistListAPIView.as_view()),
    path('add-to-wishlist/', views.AddToWishlistAPIView.as_view()),
    path('delete-from-wishlist/', views.DeleteFromWishlistAPIView.as_view())
]
