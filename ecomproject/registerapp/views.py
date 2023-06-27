from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Payment
from ecomapp.models import Product
from cart.models import Cart, CartItem
from django.contrib import messages


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def pay_detail(req, total=0, counter=0, pay_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(req))
        pay_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in pay_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(req, 'cash.html', dict(pay_items=pay_items, total=total, counter=counter))


def add_pay(req, product_id):
    product = Product.objects.get(id=product_id)
    return render(req,'cash.html',{'product':product})
