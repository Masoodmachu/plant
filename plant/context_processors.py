from plant.models import homeplants
from plant.models import fertilizer

def Links(request):
    p = homeplants.objects.all()

    return {'links':p}

def links2(request):
    f=fertilizer.objects.all()
    return {'links2':f}



