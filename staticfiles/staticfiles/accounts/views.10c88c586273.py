from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from storeApp.models import Customer
import math


@login_required(login_url='sign_in')
def home(request):
    return render(request, "index.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            this_user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not Exist')
            
        this_user = authenticate(request, username=username, password=password)
        
        if this_user is not None:
            login(request, this_user)
            return redirect('home')
            messages.success(request, "Logged In...!")
            
    context = {
        messages: 'messages',
    }
        
    return render(request, "accounts/in.html", context)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["fname"]
        surname = request.POST["surname"]
        password = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        if  password == pass2:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = surname
            
            Customer.objects.create(
                user=user,
                email=email
            )
            
            template = render_to_string("welcome.html", {'name':fname})
            
            welcome_email = EmailMessage(
                'Welcome To Online Shoppers Uganda Limited',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            welcome_email.fail_silently = False
            welcome_email.send()
            
            user.save()
            
            messages.success(request, "Account Created successfully...!")
            return redirect("sign_in")
        else:
            messages.error(request, "Passwords don't Match..!")
            return redirect("register_account")
        
    context = {
        messages: 'messages',
    }
    return render(request, "accounts/up.html", context)

def signout(request):
    logout(request)
    return redirect('home')
 