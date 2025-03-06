from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def demofunction(request):
    return render(request,"about.html")
def demofunction1(request):
    return render(request,"login.html")
def homefunction(request):
    return render(request,"index.html")
def contactfunction(request):
    return render(request,"contact.html")
def adminlogin(request):
    name=request.POST["uname"]
    password=request.POST["pwd"]
    if name=="bhargav" and password=="123":
        return render(request,"adminhome.html")
    else:
        return render(request,"unsuccessfull.html")
def register(request):
    return render(request,"register.html")
def succesfull(request):
    return render(request,"succesfull.html")


