"""models for restaurt management"""
from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    """Models for menu selection"""
    image = models.ImageField(null=True,upload_to='uploads/test/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    type = models.CharField(null=True,max_length=200)
    quantity = models.IntegerField(null=True)
    status=models.IntegerField(null=True,default=0)
    price=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Table(models.Model):
    """Models for perform CRUD operation on tables"""
    name = models.CharField(max_length=30,null=True, default="Special")
    numberofchairs = models.IntegerField()
    def __str__(self):
        return self.name+"-"+str(self.numberofchairs)

class Reservation(models.Model):
    """Models for reserving Table"""
    # user_no=models.ForeignKey(Users, on_delete=models.CASCADE)
    table_no=models.ForeignKey(Table, on_delete=models.CASCADE)
    staff_assign=models.ForeignKey(User, on_delete=models.CASCADE)
    def __int__(self):
        return self.table_no


class Orders(models.Model):
    """Models for orders made by customer"""
    staff_no=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    user_no=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user',null=True)
    table_no=models.ForeignKey(Table, on_delete=models.CASCADE)
    status=models.IntegerField(null=True)
    attend=models.IntegerField(null=True,default=0)
    date= models.DateField(null=True)
    star=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    def __int__(self):
        return str(self.status)
    
class OrderList(models.Model):
    """Models for storing the items ordered by customer"""
    menu_no=models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_no=models.ForeignKey(Orders, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)

class CustomerRequest(models.Model):
    """Model for comntact us page"""
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    staff_ad = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    status = models.IntegerField()
    comments = models.CharField(max_length=200,null=True)

    def __int__(self):
        return str(self.name)

    