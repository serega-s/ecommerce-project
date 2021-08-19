from datetime import datetime

from django.shortcuts import get_object_or_404
from ecommerce.models import Order, OrderItem, Product, ShippingAddress
from ecommerce.serializers import OrderSerializer
from rest_framework import authentication, generics, permissions
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
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

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['address'],
            phone=data['phone'],
            city=data['city'],
            postal_code=data['postal_code'],
            country=data['country'],
            shipping_price=data['shipping_price']
        )

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


class GetMyOrders(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class GetOrder(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    order.is_paid = True
    order.is_delivered = True

    order.paidAt = datetime.now()
    order.save()

    return Response('Order Confirmed')
