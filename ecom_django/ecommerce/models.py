from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    countInStock = models.IntegerField(blank=True, null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/",
                              default="placeholder.png", blank=True, null=True)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def __str__(self):
        return self.name

    @property
    def get_avg_rating(self):
        reviews = Review.objects.filter(product=self)
        count = len(reviews)
        summary = 0
        try:
            for rvw in reviews:
                summary += rvw.rating
            return (summary/count)
        except ZeroDivisionError:
            return 0

    @property
    def is_available(self):
        if self.countInStock > 0:
            return True
        return False


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    PROCESSING = 'Processing'
    DELIVERING = 'Delivering'
    DELIVERED = 'Delivered'
    NOT_DELIVERED = 'Not Delivered'
    DELIVERY_STATUS_CHOICES = (
        (PROCESSING, 'processing'),
        (DELIVERING, 'delivering'),
        (DELIVERED, 'delivered'),
        (NOT_DELIVERED, 'not_delivered'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    delivery_status = models.CharField(
        choices=DELIVERY_STATUS_CHOICES, max_length=50, default=PROCESSING)
    delivered_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def get_price_total(self):
        orderitems = self.orderitems.all()
        total = sum(
            [item.get_total + self.shipping_price for item in orderitems])

        return total

    @property
    def get_items_total(self):
        orderitems = self.orderitems.all()
        total = sum([item.quantity for item in orderitems])

        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orderitems')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True, related_name='shipping')
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self):
        return str(self.address)
