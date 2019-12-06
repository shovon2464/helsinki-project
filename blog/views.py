from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Account
from product.models import Product
from blog.models import Blog
from blog.models import ReviewBlog
from django.contrib import auth
from django.contrib.auth.decorators import login_required
User = get_user_model()

@login_required
def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_home.html', {'blogs':blogs})


@login_required
def blog_detail(request, blog_id):
    reviews = ReviewBlog.objects.all().filter(reviewed_for=blog_id)
    blog = get_object_or_404(Blog, pk=blog_id)
    product = blog.product
    product_id = product.id
    return render(request, 'blog/blog_detail.html', {'blog':blog, 'reviews':reviews, 'product_id':product_id})


@login_required
def comment_blog(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        temp = request.user
        review_detail = ReviewBlog.objects.create(reviewed_by=temp, reviewed_for = blog, review_blog=request.POST['comment_blog'])
        return redirect('/blog/'+str(blog.id))


@login_required
def reach_product(request, product_id):
    print(product_id)
    return redirect('/product/'+str(product_id))
