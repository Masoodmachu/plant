from django.urls import path
from plant_app import views
app_name='disease'

urlpatterns = [
    path('', views.index, name='index'),
]
