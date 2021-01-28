from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    context={'name':"shashank",'course':"django"}
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def project(request):
    return render(request,"project.html")

def contact(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(email,name,phone,desc)
        ins=Contact(email=email,name=name,phone=phone,desc=desc)
        ins.save()
        print("data has been writeen to DB")
    return render(request,"contact.html")
