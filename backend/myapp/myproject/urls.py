from django.urls import path
from .views import CreateProductView, ProductDetailView

urlpatterns = [
    path('products/',CreateProductView.as_view(),name='create-product'),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product-detail')
]
