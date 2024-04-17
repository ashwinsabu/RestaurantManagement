"""Operations performed from customer in restaurant"""
from django.shortcuts import render, redirect
from .models import *
from staff.models import *
from django.urls import reverse
from datetime import date
from django.db.models import Min
import random
from django.contrib import messages

# Create your views here.
#Index Page
def IndexPageView(request):
    """Index Page for customers"""
    if request.method == 'POST':
        userid = request.POST.get('userid')#retrieves the current user logged into the system
        try:
            order=Orders.objects.exclude(user_no=userid,status=5).get(user_no=userid)#check if the user has any ongoing order
            return redirect('food_status',order.id)
        except:
            return redirect('index')
    specials=Menu.objects.filter(status=1) #To display the specials menu items set by the STAFF in STAFF portal
    context = {
        'specials':specials,
    }
    return render(request, 'users/index.html',context)


#Tables page
def TablePageView(request):
    """Page for table selection"""
    if request.user.is_authenticated and request.user.is_staff == False:    #checks if user is logged in and is a CUSTOMER
        tables = Table.objects.all().values()   #Retrieves the values of all table created by ADMIN
        context = {
        'tables': tables,
        }
        return render(request, 'users/tables.html',context)
    else:
        return redirect('login') 

#menu page
def menuPageView(request, id):
    """Page to display the menu"""
    if request.user.is_authenticated and request.user.is_staff == False:    #checks if user is logged in and is a CUSTOMER
        cartList=[]
        if 'cart' in request.session:   #check if cart session is present and add the menu to the cartList which then is send to the page to display
            cartid=request.session['cart']
            for x in cartid:
                y=Menu.objects.get(id=x)
                cartList.append(y)
        if request.method == 'POST':
            if 'addcart' in request.POST:   #Checks if the add to cart button is clicked and then creates a session called cart if it does not exist and append
                # print(request.POST)
                menuid = request.POST.get('menu_id')
                menuitem = Menu.objects.get(id=menuid)
                cart = request.session.get('cart', [])
                cart.append(menuitem.id)
                request.session['cart'] = cart
                # print(request.session['cart'])
                return redirect(reverse('menu', args=[id]))
            
            elif 'removecart' in request.POST: #Remove an item from the cart
                menuid = request.POST.get('menu_id')
                menuitem = Menu.objects.get(id=menuid)
                cart = request.session.get('cart', [])
                if menuitem.id in cart:
                    cart.remove(menuitem.id)    #Remove it from the session
                    request.session['cart'] = cart
                return redirect(reverse('menu', args=[id]))
            
            elif 'submitorder' in request.POST: #Submits the order data to the  tables
                check_staff=Attendance.objects.filter(logout_time__isnull=True)     #Filters the active staff in the restaurant
                if(check_staff):    #Proceeds only if there is an active staff to take the orders
                    cart = request.session.get('cart', [])
                    if len(cart)==0:    #Checks if the submit button is clicked with some  items selected. Error message displayed if no items in cart
                        messages.info(request, "No items in cart !!")
                        return redirect(reverse('menu', args=[id]))

                    
                    table = Table.objects.get(id=id)
                    #Staff selection based on current active orders
                    staff_selc=check_staff.aggregate(minorder=Min('active_orders')) #Check value of minumum active ordercount
                    staff_final = check_staff.filter(active_orders=staff_selc['minorder']).values_list('user_id', flat=True) #Gets the list of all staff with this minimum order
                    x=random.choice(staff_final) #If there are more than one staff with same number of active order, we use random to select a staff
                    staff_no = User.objects.get(id=x)
                    currentuser = request.user
                    order = Orders.objects.create(
                            staff_no= staff_no,
                            user_no= currentuser,
                            table_no=table,
                            status=1,
                            date=date.today()
                        )
                    #So once the order is assigned active orders for a staff would increment
                    update_ordercount=Attendance.objects.get(user_id=x,logout_time__isnull=True)
                    update_ordercount.active_orders+=1
                    update_ordercount.save()
                    #As the order is created, we need to also create the orderlist and update it in the table
                    total_price=0
                    for items in cart:
                        quantity=cart.count(items)
                        if(quantity==0):
                            continue
                        carts=[]
                        carts=[value for value in cart if value != items]
                        print(carts)
                        cart=carts
                        menuitem = Menu.objects.get(id=items)
                        total_price+=menuitem.price
                        orderlist = OrderList.objects.create(
                            menu_no=menuitem,
                            order_no=order,
                            quantity=quantity
                        )
                    order.total_price=total_price
                    order.save()
                    # OrderList.objects.filter(order_no=None).update(order_no=order)
                    request.session.pop('cart', None)
                    return redirect('food_status',order.id)
                else:
                    messages.info(request, "There are no staff logged in to take up the order. Kindly contact the manager to assign a staff")

        menu = Menu.objects.all().values()
        print(menu)

        context = {'menu': menu,
                   'cartList':cartList}
        # print(cartList)
        return render(request, 'users/menu.html', context)
    else:
        return redirect('login') 


def stausfoodPageView(request,id):
    """Page to display the status of food odered by the customers"""
    if request.user.is_authenticated and request.user.is_staff == False:
        if request.method=="POST":
            # check if customer has initiated a call status
            if "staffcall" in request.POST:
                details=Orders.objects.get(id=id)
                details.attend=1
                details.save()
                return redirect('food_status',id)
            # Checks if customer has initiated a bill request
            elif "billrequest" in request.POST:
                details=Orders.objects.get(id=id)
                details.status=4    #sets the status to 4 which indicate the bill generate request
                details.save()
                # Updates the count of active orders for the staff assigend
                update_ordercount=Attendance.objects.get(user_id=details.staff_no,logout_time__isnull=True)
                update_ordercount.active_orders-=1
                update_ordercount.save()
                return redirect('food_status',id)
            # updates the rating provided by customer for the specific order
            elif "rating" in request.POST:
                details=Orders.objects.get(id=id)
                star = request.POST.get('star')
                details.star=star
                details.save()
                return redirect('index')


        details=Orders.objects.get(id=id)
        if(details.status==5):
            return redirect('index')
        # print(details.status)
        context = {
        'details': details,
    }
        return render(request, 'users/food_status.html',context)
    else:
        return redirect('login')


def contactPageView(request):
    """Managing the customer queries"""
    if(request.method=='POST'): #Creates a record in Customer Request Table after the submissoin from index.html
        name = request.POST.get('name') 
        email = request.POST.get('email')
        message = request.POST.get('message')
        orderlist = CustomerRequest.objects.create(
                    name=name,
                    email=email,
                    message=message,
                    status=0    #Sets the status to 0 for filtering the queries responded by staff or not
                )
        return redirect('index')
    return render(request, 'users/contact.html')

def AboutPageView(request):
    """Display the details of the team"""
    return render(request, 'users/about.html')

