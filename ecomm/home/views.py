from django.shortcuts import render
from products.models import Product



def index(request):

    context = {'products' : Product.objects.all()}
    return render(request , 'home/index.html' , context)
def home(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/home.html",context)
def delivery(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/delivery.html",context)
# def buynow(request):
#     context = {'products' : Product.objects.all()}
#     return render(request,"home/buynow.html",context)
from .forms import InputForm1
def buynow(request):
    submitted_details=None
    if(request.method=="POST"):
        form=InputForm1(request.POST)
            
        if form.is_valid():
            submitted_details=form.cleaned_data
        else:       
            return render(request, 'home/buynow.html', {'form':form, 'submitted_details':submitted_details})
    else:
        form=InputForm1()
    return render(request, 'home/buynow.html', {'form':form, 'submitted_details':submitted_details})
def conform(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/conform.html",context)
def payment(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/payment.html",context)
def upi(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/upi.html",context)

def net(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/net.html",context)
def order(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/order.html",context)
def profile(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/profile.html",context)
def add(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/add.html",context)
def pro(request):
    context = {'products' : Product.objects.all()}
    return render(request,"home/pro.html",context)






