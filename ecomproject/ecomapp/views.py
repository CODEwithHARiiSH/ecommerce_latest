from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage,InvalidPage,Paginator

from .models import Category, Product
from reviewapp.models import Review


# Create your views here.
def home(request):
    return render(request, "base.html")


def allprodcat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


def proddetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
        context = Review.objects.all()
        if request.method == "POST":
            name = request.POST.get('name', '')
            review = request.POST.get('review', '')
            rate = request.POST.get('rate', '')
            task = Review(name=name, review=review, rate=rate)
            task.save()
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product,'context':context})

def delete_data(request,data_id):
    context =  Review.objects.get(id=data_id)
    if request.method == 'POST':
        context.delete()
        return redirect('ecom:prodcatdetails')
    return render(request,'delete.html',{'context':context})





