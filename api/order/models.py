from django.db import models
from api.user.models import CustomUser
from api.product.models import Product

# Order Model
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_names = models.CharField(max_length=150)
    total_products = models.CharField(max_length=250, default=0)
    total_amount = models.CharField(max_length=250, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=150, default=0)
    order_confirm = models.BooleanField(default=False, verbose_name='Order Confirm')
    delivery_date_time = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return f"{self.order_confirm}"




