from django.urls import path
from .views import (
    ProductList, ProductDetail,
    product_list_functional, product_create_functional,
    ProductListClass,
    product_template_view
)

urlpatterns = [
    path('functional/list/', product_list_functional, name = 'product-list'),
    path('functional/create/', product_create_functional, name='functional-create'),
    path('class/list/', ProductListClass.as_view(), name='class-list'),
    path('class/create/', ProductListClass.as_view(), name='class-create'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('form/', product_template_view, name='product-form'),
]
