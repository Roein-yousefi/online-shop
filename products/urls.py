from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('<int:pk>/', views.ProductDetailView.as_view() , name='product_detail'),
]