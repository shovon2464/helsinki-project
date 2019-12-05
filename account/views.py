from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import Account
from django.contrib import auth
User = get_user_model()

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                #user = User.objects.get(username=request.POST['username'])
                x = User.objects.get(email=request.POST['email'])
                y = User.objects.get(email=request.POST['email'])
                if x and y:
                    return render(request, 'account/signup.html', {'error':'Username or email has already been taken'})
            except User.DoesNotExist:
                if request.POST['email'] and request.POST['username'] and request.POST['full_name'] and request.POST['address'] and request.POST['gender'] :
                    user = User.objects.create_user(email=request.POST['email'], username= request.POST['username'], password = request.POST['password1'])
                    user.full_name = request.POST['full_name']
                    user.address = request.POST['address']
                    user.gender = request.POST['gender']
                    user.profile_picture=request.FILES['profile_picture']
                    user.get_email= request.POST['get_email']

                    user.save()
                    auth.login(request,user)
                    return redirect('home')
                else:
                    return render(request, 'account/signup.html', {"error":"All fields are required"})


        else:
            return render(request, 'account/signup.html', {'error':'Password must match'})

    else:
        #the usser wants to sighup
        return render(request, 'account/signup.html')



def login(request):
    if request.method == "POST":
        user = auth.authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error':"email or password is incorrect"})

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'account/profile.html', {'user':user})

def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'account/edit.html', {'user': user})


def edit_save(request, user_id):
    if request.method == "POST":
        if request.POST['full_name'] and request.POST['address'] and request.POST['gender'] :
            user = request.user
            user.full_name = request.POST['full_name']
            user.address = request.POST['address']
            user.gender = request.POST['gender']
            if request.POST['profile_picture']:
                user.profile_picture=request.FILES['profile_picture']
            user.get_email= request.POST['get_email']
            user.save()
            return redirect('/account/'+str(user.id))
        else:
            return render(request, 'account/edit.html', {"error":"All fields are required"})

    else:
        #the usser wants to sighup
        return render(request, 'account/edit.html')
