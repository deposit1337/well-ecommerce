from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    path('category/<slug:category_slug>/<str:product_vendor>/<int:product_id>/', views.product_details, name='product_details'),

]

#
# if settings.DEBUG:
#     urlpatterns + static(settings.STATIC_URL)