from django.shortcuts import render,HttpResponse

# Create your views here.
def response_customer(request):
    return HttpResponse("Hello from customer page")
