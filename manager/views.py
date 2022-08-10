from django.shortcuts import render,redirect
from base.models import ReservationForm,Contact
# Create your views here.

def reservation_list(request):
    not_reserv = ReservationForm.objects.filter(is_processed=False)
    return render(request, "reservation_list.html", context={
        "unreserv_list":not_reserv,
    }
        )

def update_reservation(request,pk):
    ReservationForm.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:reservations_list")

def contact_func(request):
    unreviewed=Contact.objects.filter(done=False)
    return render(request,"contacts.html",context={
        "unreview_message":unreviewed,
    }
      )
def update_contact(request,pk):
    Contact.objects.filter(pk=pk).update(done=True)
    return redirect("manager:contact_func")