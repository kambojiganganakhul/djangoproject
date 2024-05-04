from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email



class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to = 'profile')

class Coupon(BaseModel):
    coupon_code=models.CharField(max_length=10)
    id_expired=models.BooleanField(default=False)
    discount_price=models.IntegerField(default=100)
    minimun_amount=models.IntegerField(default=500)

@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)
        
class Cart(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    COUPON = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    
    def get_cart_total(self):
        cart_items=self.cart_items.all()
        price=[]
        for cart_item in cart_items:
            price.append(cart_item.product.price)
            
            if cart_item.color_variant:
                color_variant_price=cart_items.color_variant.price
                
                price.append(color_variant_price)
            # if cart_item.size_variant:
            #     color_variant_price=cart_items.size_variant.price
                
            #     price.append(size_variant_price)
        return sum(price)
        
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Coupon, on_delete=models.CASCADE)  # Assuming Product model exists
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"CartItem - {self.product}"

    def get_total_price(self):
        if self.color_variant:
            return self.product.price * self.quantity + self.color_variant.price
        else:
            return self.product.price * self.quantity