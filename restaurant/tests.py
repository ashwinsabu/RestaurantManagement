from datetime import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *

# Create your tests here.
class TestModels(TestCase):
    """Class for testing the models section"""
    def setUp(self):
        """Function for initilaizing user to be used accross the class"""
        self.user1= User.objects.create_user(username='nci2024', password='peaceinworld')
        self.user2= User.objects.create_user(username='staff_2024', password='peaceinworld')
        self.table_datas= Table.objects.create(name='Test',numberofchairs=10)
        self.menu_data = Menu.objects.create(image='./image/test_image.jpg',name='Test',description="Test Description",type= 'veg',quantity=10,status=10,price=200)
        self.order_data = Orders.objects.create(staff_no=self.user1,user_no=self.user2,table_no=self.table_datas,status=0)
		
    def test_model_menu(self):
        """Function for creating menu contents"""
        bid_item = Menu.objects.create(
            image='./image/test_image.jpg',
			name='Test',
			description="Test Description",
			type= 'veg',
            quantity=10,
            status=10,
            price=200,
		)
        self.assertEqual(str(bid_item), 'Test')
        self.assertTrue(isinstance(bid_item,Menu))
    
    def test_model_table(self):
        """Function for creating table"""
        table_data = Table.objects.create(
			name='Test',
            numberofchairs=10,
		)
        self.assertEqual(str(table_data), 'Test-10')
        self.assertTrue(isinstance(table_data,Table))
        
    def test_model_reservation(self):
        """Function for adding reservation"""
        table_data = Reservation.objects.create(
			table_no=self.table_datas,
            staff_assign=self.user2,
		)
        self.assertTrue(isinstance(table_data,Reservation))
    
    def test_model_orders(self):
        """Function for creating orders"""
        order_data = Orders.objects.create(
            staff_no=self.user1,
            user_no=self.user2,
            table_no=self.table_datas,
            status=0,
		)
        self.assertTrue(isinstance(order_data,Orders))
        
    def test_model_orderlist(self):
        """Function for creating order list"""
        order_data = OrderList.objects.create(
            menu_no=self.menu_data,
            order_no=self.order_data,
            quantity=10,
		)
        self.assertTrue(isinstance(order_data,OrderList))
        
    def test_model_customer(self):
        """Function for creating cusotmer query"""
        customer_data = CustomerRequest.objects.create(
            name="Ashwin",
            email="ashwin@ashwin.com",
            message="Test",
            staff_ad=self.user1,
            status=0,
		)
        self.assertTrue(isinstance(customer_data,CustomerRequest))
    