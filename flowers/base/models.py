from django.db import models

class category(models.Model):
   name=models.CharField(max_length=23)
   def __str__(self):
      return self.name

class flower(models.Model):
    flowername=models.CharField(max_length=25)
    category=models.ForeignKey(category, on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to ='photos/flowers')
    slug=models.SlugField(max_length=25,unique=True)

    def __str__(self):
       return self.flowername

class customer(models.Model):
   flower=models.ForeignKey(flower,on_delete=models.CASCADE,blank=True,null=True)
   firstname=models.CharField(max_length=25)
   lastname=models.CharField(max_length=25)
   address=models.CharField(max_length=35)
   def __str__(self):
      return f"{self.firstname} {self.address}"


class contactform(models.Model):
   firstname=models.CharField(max_length=25)

   customer=models.ForeignKey(customer,on_delete=models.CASCADE,blank=True,null=True)
   email=models.EmailField()
   phone=models.IntegerField()
   message=models.CharField(max_length=20)
   def __str__(self):
      return self.firstname 

class Order(models.Model):
   orderid=models.IntegerField()
   customer=models.ForeignKey(customer,on_delete=models.CASCADE,blank=True,null=True)
   ocassion=models.CharField(max_length=30)
   complete=models.BooleanField(default=False)
   def __str__(self):
      return str( self.orderid)
   class Meta:
      ordering=['complete']
      
   
class BookingForm(models.Model):
   bookingnumber=models.IntegerField()
   orderform=models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
   firstname=models.CharField(max_length=25)
   lastname=models.CharField(max_length=25)
   
   def __str__(self):
      return str(self.bookingnumber) 
