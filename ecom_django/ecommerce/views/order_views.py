from datetime import datetime

from django.shortcuts import get_object_or_404
from ecommerce.models import Order, OrderItem, Product, ShippingAddress
from ecommerce.serializers import OrderSerializer
from rest_framework import authentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data

    orderitems = data['orderitems']

    if orderitems and len(orderitems) == 0:
        return Response({'detail': 'No Order Items'}, status=400)
    else:
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            shipping_price=data['shipping_price'],
            total_price=data['total_price']
        )

        print('SHIPPING PRICE:', data['shipping_price'])

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['address'],
            phone=data['phone'],
            city=data['city'],
            postal_code=data['postal_code'],
            country=data['country'],
            shipping_price=data['shipping_price']
        )

        # for loop for every item in our order items
        for i in orderitems:
            product = Product.objects.get(id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                quantity=i['quantity'],
                price=i['price'],
                image=product.image.url,
            )

            product.countInStock -= int(item.quantity)
            product.save()

        current_order = user.orders.last()

        serializer = OrderSerializer(current_order)

        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    order.is_paid = True
    order.is_delivered = True

    order.paidAt = datetime.now()
    order.save()

    return Response('Order Confirmed')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    user = request.user
    orders = user.orders.all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    serializer = OrderSerializer(order)

    return Response(serializer.data)
