
from django.contrib import admin
from django.urls import path, include
from cart import views
app_name='cart'
urlpatterns = [
    path('addtocart/<int:p>',views.addtocart,name='addtocart'),
    path('cartview/',views.cartview,name='viewcart'),
    path('removecart/<int:p>',views.removecart,name='removecart'),
    path('deletecart/<int:p>',views.deletecart,name='deletecart'),
    path('order/',views.orderform,name='orderform'),
    path('vieworder/',views.orderview,name='orderview'),
    path('det/',views.det,name="det"),
    # path('payment/',views.payments,name='payment'),
    # path('payment_status/',views.payment_status,name='payment_status')
    path('payment/', views.payments, name="mypay"),
    path('sucess/', views.payment_status, name="success"),



]
