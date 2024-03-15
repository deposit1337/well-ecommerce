from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
]