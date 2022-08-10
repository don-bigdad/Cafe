from django.shortcuts import render,redirect
from .models import *
from .forms import ReservationForm,Contact
# Create your views here.

def response_base(request):
    if request.method == "POST":
        if not ReservationForm == None:
            reservation = ReservationForm(request.POST)
            if reservation.is_valid():
                reservation.save()
                return redirect('/')
        else:
            contact = Contact.objects.all()
            contact.save()
            return redirect("/")

    categories = Category.objects.all()
    dishes = Dish.objects.all()
    specials = Specials.objects.all()
    events = Event.objects.all()
    about = AboutUs.objects.all()
    photo = Galery.objects.all()
    video = VideoAboutUs.objects.all()
    reservation = ReservationForm()
    contacts = Contact()
    data ={"categories":categories,"dishes":dishes,"events":events,"specials":specials,"about":about,"photo":photo,
           "video":video,'reservation_form':reservation,"contacts":contacts
           }
    return render(request,"base.html",context=data)