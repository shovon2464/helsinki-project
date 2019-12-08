from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from django.utils import timezone
from django.conf import settings
from product.models import Product
User = get_user_model()




class Cart(models.Model):
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE)
    bought_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.bought_product.name}'

    def get_total(self):
        total = self.bought_product.p_price() * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal


class Order(models.Model):
    ordered_products = models.ManyToManyField(Cart)
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.bought_by.username

    def get_totals(self):
        total = 0
        for order_item in self.ordered_products.all():
            total += order_item.get_total()

        return total
