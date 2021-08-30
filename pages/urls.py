from django.urls import path, include

from pages.views import HomeView, WishlistListView, add_to_wishlist, ContactCreateView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),

]
