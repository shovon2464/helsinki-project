from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from product.models import Product
from django.utils import timezone
from django.conf import settings
User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def title_summary(self):
        return self.body[:100]

    def pub_date_smart(self):
        return self.pub_date.strftime('%b %e, %y')

class ReviewBlog(models.Model):
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_for = models.ForeignKey(Blog, on_delete=models.CASCADE)
    review_blog = models.TextField(max_length=1000)
