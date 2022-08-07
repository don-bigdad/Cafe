from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def response_base(request):
    categories = Category.objects.all()
    dish = Dish.objects.all()
    specials = Specials.objects.all()
    events = Event.objects.all()
    about = AboutUs.objects.all()
    photo = Galery.objects.all()
    data ={"categories":categories,"dish":dish,"events":events,"specials":specials,"about":about,"photo":photo,}
    return render(request,"base.html",context=data)