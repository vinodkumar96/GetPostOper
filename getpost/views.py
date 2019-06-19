from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput (request):
    return render(request,"getinput.html")
def postinput (request):
    return render(request,"postinput.html")
def add (request):
    if request.method == "GET":
        try:
            a=request.GET["t1"]
            b=request.GET["t2"]
            c=int(a)
            d=int(b)
            e=c+d
            return HttpResponse("the sum is:" +str(e))
        except(ValueError):
            return HttpResponse("invalid input")
    else:
        try:
            a=request.POST["t1"]
            b=request.POST["t2"]
            c=int(a)
            d=int(b)
            e=c+d
            return HttpResponse("the sum is:" +str(e))
        except(ValueError):
            return HttpResponse("invalid input")

