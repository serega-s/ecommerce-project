from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from ecommerce.models import Product, Review
from ecommerce.serializers import ProductSerializer
from rest_framework import authentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    review = Review.objects.create(
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

    products = Product.objects.filter(Q(name__icontains=query) | Q(
        description__icontains=query)).order_by('-created_at')

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
