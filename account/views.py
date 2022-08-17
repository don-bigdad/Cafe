from django.shortcuts import render,redirect
from .forms import UserRegistration,UserLogin
from django.contrib.auth import authenticate,login,logout

def login_user(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get("next")
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        next_post = request.POST.get("next")
        return redirect(next_get or next_post or "/")
    return render(request,"login.html",context={"form":form})
def logout_user(request):
    logout(request)
    return redirect("/")

def registration_user(request):
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        return redirect("/")
    return render(request,"register.html",context={"form":form})
