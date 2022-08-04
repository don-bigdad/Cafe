from django.shortcuts import render,HttpResponse

# Create your views here.
def response_base(request):
    return HttpResponse("Hello from base page")