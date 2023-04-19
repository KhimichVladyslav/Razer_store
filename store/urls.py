from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Домашня сторінка
    path('', views.home, name='home'),

    # Показує всі товари
    path('all_products/', views.all_products, name='all_products'),
    path('all_products_by_price_min/', views.all_products_by_price_min, name='all_products_by_price_min'),
    path('all_products_by_price_max/', views.all_products_by_price_max, name='all_products_by_price_max'),

    # Шукає товари
    path('search/', views.search, name='search'),

    # в slug приходить назва товару та перенаправляє у вьюху
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
