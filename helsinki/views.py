from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Account
from django.contrib import auth
User = get_user_model()


def home(request):
    return render(request, 'home.html')
