from django.shortcuts import render
from home.models import login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"Hello.html")

def Login(request):

    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('country'):
            print(request.POST.get('name'))
            saverecord=login()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.country=request.POST.get('country')
            saverecord.save()
            messages.success(request,'Submitted Successfylly')
            return render(request,"test.html")
    else:
        return render(request,"test.html")