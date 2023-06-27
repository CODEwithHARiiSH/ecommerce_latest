from . import views

from django.urls import path, include
app_name='cred'

urlpatterns = [


    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index/',views.index,name='index'),
    path('payment/', views.payy, name='payment'),
    path('last/',views.payy, name='p')

]
