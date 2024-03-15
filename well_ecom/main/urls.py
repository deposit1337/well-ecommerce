from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    # path('catalog/<str:pk>/', views.catalog, name='catalog'),
    # path('catalog/item-page', views.item_page, name='item'),
]