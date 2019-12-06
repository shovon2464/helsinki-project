from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Account
from django.contrib import auth
from product.models import Product
from product.models import Category
from product.models import Review
from django.contrib.auth.decorators import login_required
User = get_user_model()


@login_required
def product_home(request):
    products = Product.objects.all()
    return render(request, 'product/product_home.html', {'products':products})

@login_required
def detail(request, product_id):
    reviews = Review.objects.all().filter(reviewed_for=product_id)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product':product, 'reviews':reviews})


@login_required
def comment_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        temp = request.user
        review_detail = Review.objects.create(reviewed_by=temp, reviewed_for = product, review=request.POST['comment_product'])
        return redirect('/product/'+str(product.id))
