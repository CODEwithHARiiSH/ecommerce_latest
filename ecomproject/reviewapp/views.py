from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *


# Create your views here.
def review(request):
    context = Review.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        review = request.POST.get('review', '')
        rate = request.POST.get('rate', '')
        task = Review(name=name, review=review, rate=rate)
        task.save()
        return redirect('ecom:prodcatdetails')
    return render(request, 'product.html', {'context': context})



