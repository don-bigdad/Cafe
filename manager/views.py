from django.shortcuts import render,HttpResponse

# Create your views here.
def response_manager(request):
    return HttpResponse("Hello from manager page")