from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),

    path('all_products/', views.all_products, name='all_products'),
    path('all_products_by_price_min/', views.all_products_by_price_min, name='all_products_by_price_min'),
    path('all_products_by_price_max/', views.all_products_by_price_max, name='all_products_by_price_max'),

    path('search/', views.search, name='search'),

    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
