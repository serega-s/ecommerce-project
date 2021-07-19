from django.contrib.auth.models import User
from django.db import models
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from ecommerce.models import Order, OrderItem, Product, Review, ShippingAddress


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

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email'
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = (
            'id',
            'product', 
            'user', 
            'rating', 
            'comment', 
            'created_at'
        )



class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = (
            'id', 
            'name', 
            'brand', 
            'get_avg_rating',
            'price', 
            'description', 
            # 'rating', 
            'countInStock', 
            'get_image', 
            'reviews'
        )


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only=True)
    shipping_address = ShippingAddressSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'user',
            'order_items',
            'shipping_address',

            'id',
            'paymentMethod',
            'shipping_price',
            'total_price',
            'is_paid',
            'paid_at',
            'is_delivered',
            'delivered_at',
            'created_at'
        )
    
