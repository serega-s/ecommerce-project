from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query_utils import Q
from django.http.response import Http404
from ecommerce.models import *
from ecommerce.models import Product, Review
from ecommerce.serializers import ProductSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
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
    serializer = ProductSerializer(products, many=True)

    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


class AddComment(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request, product_id, format=None):
        product = self.get_object(product_id)

        review = Review.objects.create(
            user=request.user,
            product=product,
            rating=request.data['rating'],
            comment=request.data['comment']
        )
        serializer = ProductSerializer(product)

        return Response(serializer.data)
