from django.shortcuts import render,redirect
from base.models import ReservationForm
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