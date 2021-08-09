from django.urls import path

from .views import product_views, order_views

urlpatterns = [
    ### products
    path('products/', product_views.products_list),
    path('products/<int:product_id>/', product_views.product_detail),
    path('products/<int:product_id>/add_comment/', product_views.add_comment),

    ### orders
    path('products/add_order_items/', order_views.add_order_items),
    path('orders/my-orders/', order_views.get_my_orders),
    path('orders/<int:order_id>/', order_views.get_order),
    path('orders/confirm-order/<int:order_id>/', order_views.confirm_order),
]
