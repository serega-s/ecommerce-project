from django.urls import path

from .views import order_views, product_views

urlpatterns = [
    # products
    path('products/', product_views.products_list),
    path('products/<int:product_id>/', product_views.ProductDetail.as_view()),
    path('products/<int:product_id>/add_comment/',
         product_views.AddComment.as_view()),

    # orders
    path('orders/add_order_items/', order_views.add_order_items),
    path('orders/my-orders/', order_views.GetMyOrders.as_view()),
    path('orders/<int:order_id>/', order_views.GetOrder.as_view()),
    path('orders/confirm-order/<int:order_id>/', order_views.confirm_order),
]
