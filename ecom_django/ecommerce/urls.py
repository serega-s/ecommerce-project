from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('products/<int:product_id>/', views.product_detail),
    path('products/<int:product_id>/add_comment/', views.add_comment),
    # path('products/search/', views.search),
    path('products/add_order_items/', views.add_order_items),
    path('my-orders/', views.get_my_orders),
    path('order/<int:order_id>/', views.get_order),
    path('order/confirm-order/<int:order_id>/', views.confirm_order),
    path('last-order/', views.get_last_order)
]
