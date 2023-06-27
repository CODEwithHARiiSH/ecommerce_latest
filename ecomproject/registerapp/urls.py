from django.urls import path
from . import views
app_name='pay'
urlpatterns=[
    path('payy/',views.pay_detail,name='pay_detail'),
    path('payyy/<int:product_id>/',views.add_pay,name='add_pay'),

]