from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import *
from cart.views import _cart_id


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('ecom:allprodcat')
        else:
            messages.info(request, "Invalid Credentials. If you are not register please register")
            return redirect('cred:login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username was Taken")
                return redirect('cred:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This Email is already exist")
                return redirect('cred:register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)

                user.save();
                print("user created")
                messages.info(request, "User created")
                return redirect('cred:login')
        else:
            messages.info(request, "password donot match")
            return redirect('cred:register')
        return redirect('ecom:allprodcat')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('ecom:allprodcat')

def index(request):

    return render(request,'index.html')
def pay(request):

    return render(request,'payment.html')


def payy(req, pay_items=None):
    cart = Cart.objects.get(cart_id=_cart_id(req))
    pay_items = CartItem.objects.filter(cart=cart, active=True)
    pay_items.delete()
    return render(req,'payment.html')

