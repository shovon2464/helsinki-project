from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from django.utils import timezone
from django.conf import settings
User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length = 500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='proudct_image/', default='default_product.png')
    details = models.TextField(verbose_name='detials')
    intro = models.TextField(verbose_name='intro')
    price = models.FloatField()
    discount = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


    def present_price(self):
        discount_percent = 100-self.discount
        p_price = self.price*(discount_percent/100)
        return p_price

    def pub_date_smart(self):
        return self.pub_date.strftime('%b %e %y')


    def offer(self):
        if self.discount>0:
            return str(self.discount)+'% discount'
        else:
            return 'Regular Product'


class Review(models.Model):
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_for = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)





class ReviewManager(models.Manager):
    def create_review(self, reviewed_by, reviewed_for, review):
        review_detail = self.model(
        reviewed_by = reviewed_by,
        reviewed_for = reviewed_for,
        review = review
        )
        review_detail.save(using=self._db)
