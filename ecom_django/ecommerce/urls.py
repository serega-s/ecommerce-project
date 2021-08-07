from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('products/<int:product_id>/', views.product_detail),
    path('products/<int:product_id>/add_comment/', views.add_comment),
    path('products/add_order_items/', views.add_order_items),
    path('orders/my-orders/', views.get_my_orders),
    path('orders/<int:order_id>/', views.get_order),
    path('orders/confirm-order/<int:order_id>/', views.confirm_order),
    path('orders/last-order/', views.get_last_order)
]
