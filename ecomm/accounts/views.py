from cmath import log
from tkinter import E

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
from django.shortcuts import get_object_or_404

from .models import Cart, CartItem
from products.models import Product

def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/home')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/register.html')

def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        
        # Check if the product already exists in the cart
        if cart.items.filter(product=product).exists():
            cart_item = cart.items.get(product=product)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        
        return redirect('cart:view_cart')

def remove_from_cart(request, cart_item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        cart_item.delete()
        return redirect('cart:view_cart')

def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})
