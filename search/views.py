from django.db.models import Q
from django.shortcuts import render
from plant.models import homeplants,Product

# Create your views here.

def search(request):
    p=None
    q=""
    if(request.method=='POST'):
      query=request.POST['q']
      # k = homeplants.objects.filter(Q(name__icontains=query))
      p=Product.objects.filter(Q(name__icontains=query))
    return render(request,"search.html",{'p':p,'q':query})