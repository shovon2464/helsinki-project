from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Account
from django.contrib import auth
from product.models import Product
from product.models import Category
from product.models import Review
from cart.models import Cart
from cart.models import Order
from django.contrib.auth.decorators import login_required
User = get_user_model()





@login_required
def add_to_cart(request, product_id):
    bought_product = get_object_or_404(Product, pk=product_id)
    ordered_product, created_time = Cart.objects.get_or_create(
             bought_product = bought_product,
             bought_by = request.user
    )
    order_check = Order.objects.filter(bought_by=request.user, ordered=False)
    if order_check.exists():
        order = order_check[0]
        if order.ordered_products.filter(bought_product=bought_product).exists():
            ordered_product.quantity = request.POST['quantity']
            ordered_product.save()
            return redirect('/product/'+str(product_id))
        else:
            order.ordered_products.add(ordered_product)
            ordered_product.quantity = request.POST['quantity']
            ordered_product.save()
            return redirect('/product/'+str(product_id))

    else:
        order = Order.objects.create(
             bought_by = request.user)
        order.ordered_products.add(ordered_product)
        ordered_product.quantity = request.POST['quantity']
        ordered_product.save()
        ordered_product = None
        return redirect('/product/'+str(product_id))


@login_required
def add_to_cart2(request, product_id):
    bought_product = get_object_or_404(Product, pk=product_id)
    ordered_product, created_time = Cart.objects.get_or_create(
             bought_product = bought_product,
             bought_by = request.user
    )
    order_check = Order.objects.filter(bought_by=request.user, ordered=False)
    if order_check.exists():
        order = order_check[0]
        if order.ordered_products.filter(bought_product=bought_product).exists():
            ordered_product.quantity = request.POST['quantity']
            ordered_product.save()
            products = Product.objects.all()
            return redirect('product/product_home.html', {'products':products})
        else:
            order.ordered_products.add(ordered_product)
            ordered_product.quantity = request.POST['quantity']
            ordered_product.save()
            products = Product.objects.all()
            return redirect('product/product_home.html', {'products':products})

    else:
        order = Order.objects.create(
             bought_by = request.user)
        order.ordered_products.add(ordered_product)
        ordered_product.quantity = request.POST['quantity']
        ordered_product.save()
        ordered_product = None
        products = Product.objects.all()
        return redirect('product/product_home.html', {'products':products})


@login_required
def cart_home(request):
    products = Product.objects.all()
    carts = Cart.objects.filter(bought_by=request.user)
    orders = Order.objects.filter(bought_by = request.user, ordered=False)
    if carts.exists() and orders.exists():
        print('done')
        order = orders[0]
        return render(request, 'cart/cart_home.html', {'order':order, 'carts':carts, 'products':products})
    else:
        return redirect('/product/all', {'products':products})



@login_required
def reach_product_home(request):
    products = Product.objects.all()
    return redirect('/product/all', {'products':products})


@login_required
def proceed(request, order_id):
    products = Product.objects.all()
    orders = Order.objects.filter(bought_by = request.user, pk=order_id)
    order = orders[0]
    order.ordered = True
    order.save()
    Cart.objects.all().delete()
    return redirect('/product/all', {'products':products})
