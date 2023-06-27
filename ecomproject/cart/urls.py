from django.urls import path
from . import views
app_name='cart'
urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('delete_cart_item/<int:product_id>/',views.delete_cart_item,name='delete_cart_item'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('ckeckout/',views.checkout,name='checkout'),
    path('',views.cart_detail,name='cart_detail'),

]