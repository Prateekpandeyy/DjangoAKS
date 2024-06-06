from django.shortcuts import render
from django.http import HttpResponse
#from attendance.models import Contact

def runFirstPro(request):
    return render(request, 'home.html')

def showMyname(request):
    return render(request, 'name.html')
    # return HttpResponse("My name is Harsh")

def addBoot(request):
    return render(request, "bootstr.html")
def contactUs(request):
    return render(request, 'contact.html')

def aboutMe(request):
    # if(request.method == "POST"):
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     print(name, email)
    #     ins = Contact(name = name, email = email)
    #     ins.save()
    return render(request, 'about.html', context ={'name' : "prateek", "age" : 20})


# Create your views here.
