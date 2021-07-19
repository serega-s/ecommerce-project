from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions, status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ecommerce.models import Order, OrderItem, Product, Review, ShippingAddress

from .serializers import OrderSerializer, ProductSerializer


@api_view(['GET'])
@permission_classes([AllowAny,])
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    Review.objects.create(
        user=request.user, 
        product=product, 
        rating=request.data['rating'],
        comment=request.data['comment']
    )
    serializer = ProductSerializer(product)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def products_list(request):
    query = request.data.get('query')
    if query == None:
        query = ''

    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).order_by('-created_at')

    page = request.query_params.get('page')
    paginator = Paginator(products, 2)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = ProductSerializer(products, many=True)

    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data

    order_items = data['order_items']

    if order_items and len(order_items) == 0:
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
            city=data['city'],
            postal_code=data['postal_code'],
            country=data['country']
        )

        # for loop for every item in our order items
        for i in order_items:
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

        serializer = OrderSerializer(order, many=False)
        
        return Response({'data': 'Order Confirmed'}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)