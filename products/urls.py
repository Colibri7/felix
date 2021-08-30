from django.urls import path

from products.views import ProductListView, ProductDetailView, add_to_cart, CartListView, CommentCreateView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]
