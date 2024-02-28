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
    path('order/<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('reply-driver-create/', views.ReplyDriverCreateAPIView.as_view()),
    path('reply-driver-list-for-client/', views.ReplyDriverListAPIViewForClient.as_view()),
    path('reply-list-for-driver/', views.ReplyDriverListAPIViewForDriver.as_view()),
    path('give-work/', views.GiveWorkAPIViewForClient.as_view()),
    path('order-list-for-map/', views.OrderListViewForMap.as_view()),
    path('wish-list/', views.ClientWishlistListAPIView.as_view()),
    path('add-to-wishlist/', views.ClientAddToWishlistAPIView.as_view()),
    path('delete-from-wishlist/<str:pk>/', views.ClientDeleteFromWishlistAPIView.as_view()),
    path('order-filter/', views.FilterOrderListAPIView.as_view())
]
