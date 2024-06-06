from django.shortcuts import render
from django.http import HttpResponse
from attendance.models import ContactUs
#from attendance.models import Contact

def runFirstPro(request):
    return render(request, 'home.html')

def showMyname(request):
    return render(request, 'name.html')
    # return HttpResponse("My name is Harsh")

def addBoot(request):
    return render(request, "bootstr.html")
def contactUs(request):
    print("request", request)
    if(request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        ins = ContactUs(email = email, password = password, address1 = address1, address2 = address2, city = city)
        ins.save()

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
