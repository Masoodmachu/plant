from django.contrib.auth.models import User
from django.db import models
from plant.models import Product,homeplants

# Create your models here.


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def totalsum(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name



class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.BigIntegerField()
    item_count=models.BigIntegerField()
    ordered_date=models.DateTimeField(auto_now_add=True)
    delivery_status=models.CharField(max_length=35,default='pending')
    order_status=models.CharField(max_length=35,default='pending')


    def __str__(self):
        return self.user.username

class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=35)
    amount=models.BigIntegerField()

    def __str__(self):
        return str(self.account_number)


class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    house = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=255, default='India')
    message_to_seller = models.TextField(blank=True, null=True)
    item_count = models.BigIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=35, default='pending')
    order_status = models.CharField(max_length=35, default='pending')

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount=models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
