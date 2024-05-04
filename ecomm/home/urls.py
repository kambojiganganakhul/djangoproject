from django.urls import path
from home.views import index
from home.views import home
from home.views import delivery
from home.views import buynow
from home.views import conform
from home.views import payment
from home.views import upi
from home.views import profile
from home.views import net
from home.views import order
from home.views import add
from home.views import pro
urlpatterns = [
    path('' , index , name="index"),
    path('home/',home, name="home"),
    path('delivery/',delivery,name="delivery"),
    path('buynow/',buynow,name="buynow"),
    path('conform/',conform,name="conform"),
    path('payment/',payment,name="payment"),
    path('upi/',upi,name="upi"),

    path('net/',net,name="net"),
    path('order/',order,name="order"),
    path('profile/',profile,name="profile"),
    path('add/',add,name="add"),
    path('pro/',pro,name="pro"),
]
