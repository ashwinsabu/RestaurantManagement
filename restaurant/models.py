from django.db import models


# class Users(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=30)

class Staffs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Menu(models.Model):
    image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=30,null=True, default="Special")
    numberofchairs = models.IntegerField()
    def __str__(self):
        return self.name+"-"+str(self.numberofchairs)

class Reservation(models.Model):
    # user_no=models.ForeignKey(Users, on_delete=models.CASCADE)
    table_no=models.ForeignKey(Table, on_delete=models.CASCADE)
    staff_assign=models.ForeignKey(Staffs, on_delete=models.CASCADE)
    def __int__(self):
        return self.table_no

class Orders(models.Model):
    reservation_no=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    table_no=models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_no=models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __int__(self):
        return self.reservation_no

    