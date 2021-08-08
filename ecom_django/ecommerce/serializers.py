from django.contrib.auth.models import User
from django.db import models
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Order, OrderItem, Product, Review, ShippingAddress


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        )


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'full_name',
        ]

    def get_full_name(self, obj):
        full_name = f'{obj.first_name} {obj.last_name}'

        return full_name


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'brand',
            'get_avg_rating',
            'is_available',
            'price',
            'description',
            'countInStock',
            'get_image',
            'reviews'
        ]


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    shipping = ShippingAddressSerializer(read_only=True)
    orderitems = OrderItemSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'paymentMethod',
            'shipping_price',
            'total_price',
            'is_paid',
            'paid_at',
            'delivery_status',
            'delivered_at',
            'created_at',
            'orderitems',
            'shipping',
            'get_price_total',
            'get_items_total'
        )
