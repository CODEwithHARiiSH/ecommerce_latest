from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='category',blank=True)
    desc=models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('ecom:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='category',blank=True)
    image1 = models.ImageField(upload_to='category', blank=True)
    image2 = models.ImageField(upload_to='category', blank=True)
    image3 = models.ImageField(upload_to='category', blank=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('ecom:prodcatdetails', args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.name)


class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rate = models.TextField()