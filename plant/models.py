from django.db import models

# Create your models here.




class Categoryplant(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=45)
    desc=models.TextField()
    image=models.ImageField(upload_to='category/images',blank=True,null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=400)
    desc=models.TextField()
    image1=models.ImageField(upload_to="product/images",blank=True,null=True)
    image2 = models.ImageField(upload_to="product/images", blank=True, null=True)
    image3 = models.ImageField(upload_to="product/images", blank=True, null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    offer_price = models.DecimalField(decimal_places=2, max_digits=10)
    specification = models.TextField()
    category=models.ForeignKey(Categoryplant,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class homeplants(models.Model):
    name=models.CharField(max_length=45)
    desc=models.TextField()
    startprice=models.IntegerField()
    image1=models.ImageField(upload_to='home/images',blank=True,null=True)
    image2=models.ImageField(upload_to='home/images',blank=True,null=True)
    image3=models.ImageField(upload_to='home/images',blank=True,null=True)
    stock=models.IntegerField(default=2)
    category = models.ForeignKey(Categoryplant,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class fertilizer(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image1 = models.ImageField(upload_to="fertilizer/images", blank=True, null=True)
    image2 = models.ImageField(upload_to="fertilizer/images", blank=True, null=True)
    image3 = models.ImageField(upload_to="fertilizer/images", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categoryplant,on_delete=models.CASCADE)
    def __str__(self):
        return self.name




# class categoryfertilizer(models.Model):
#     id=models.IntegerField(auto_created=True,primary_key=True)
#     name=models.CharField(max_length=50)
#     desc=models.TextField()
#     image1=models.ImageField(upload_to='category/fertilizer',blank=True,null=True)
#     image2=models.ImageField(upload_to='category/fertilizer',blank=True,null=True)
#     image3 = models.ImageField(upload_to='category/fertilizer', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#


