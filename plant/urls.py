
from django.contrib import admin
from django.urls import path, include
from plant import views
app_name='plant'

urlpatterns = [

   path('',views.home,name='home'),
   path('products/',views.products,name="products"),
   path('indoor/',views.indoor,name="indoor"),
   path('outdoor/',views.outdoor,name="outdoor"),
   path('login/',views.login,name='login'),
   path('register/',views.registeration,name='register'),
   path('logout/',views.logout,name='logout'),
   # path('fertilizer/',views.fertilizers,name='fertilizer'),
   path('details/<int:pk>',views.fertdet,name='detail'),
   path('fertilizer/', views.fertilizers, name='fertilizer'),


]
