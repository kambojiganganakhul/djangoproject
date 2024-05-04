from django.urls import path
from accounts.views import login_page,register_page , activate_email
from .models import Cart, CartItem
urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   
   path('base1.html', login_page, name='base1')
]
