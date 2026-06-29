
from django.contrib import admin
from django.urls import path, include
from search import views
app_name='search'
urlpatterns = [

   path('search/',views.search,name="searchproducts"),

]
