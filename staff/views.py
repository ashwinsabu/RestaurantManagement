from django.shortcuts import render,redirect
from restaurant.models import *
from .models import*
from datetime import datetime,date
from django.utils.timezone import localtime, make_aware
from django.db.models import Sum
from django.contrib.auth import logout
from employee_pkg import best_employee #Library created and imported


# Create your views here.
def StaffIndex(request):
    """To display the index page of the staff section"""
    if request.user.is_authenticated and request.user.is_staff == True:
        if request.method=='POST':
            if "prev" in request.POST:
                orderid = request.POST.get('order_id')
                order=Orders.objects.get(id=orderid)
                if(order.status>1):
                    order.status=order.status-1
                print(request.method)
                order.save()
                return redirect('index_staff') 
            
            elif "next" in request.POST:
                orderid = request.POST.get('order_id')
                order=Orders.objects.get(id=orderid)
                if(order.status<5):
                    order.status=order.status+1
                order.save()
                return redirect('index_staff')
            elif 'attend' in request.POST:
                orderid = request.POST.get('order_id')
                order=Orders.objects.get(id=orderid)
                order.attend=0
                order.save()
                return redirect('index_staff')
            elif "finish" in request.POST:
                orderid = request.POST.get('order_id')
                order=Orders.objects.get(id=orderid)
                order.status=order.status+1
                order.save()
                update_ordercount=Attendance.objects.get(user_id=request.user,logout_time__isnull=True)
                update_ordercount.active_orders-=1
                update_ordercount.save()
                return redirect('index_staff')
        
            elif "login" in request.POST:
                data=Attendance.objects.create(
                    user_id=request.user,
                    login_time=make_aware(datetime.now())
                )
                return redirect('index_staff')
            
            elif "logout" in request.POST:
                initiate=Attendance.objects.get(user_id=request.user,logout_time__isnull=True)
                initiate.logout_time=make_aware(datetime.now())
                hours = (localtime(initiate.logout_time) - localtime(initiate.login_time)).total_seconds()
                hours=int(hours / 3600)
                initiate.hours=hours
                print(hours)
                initiate.save()
                return redirect('index_staff')


        orders=Orders.objects.exclude(staff_no=request.user,status=5).filter(staff_no=request.user)
        orders_today=Orders.objects.filter(staff_no=request.user,date=date.today())
        # #Check the total star ratings
        # star=Orders.objects.filter(staff_no=request.user,star__isnull=False)
        # star_sum = star.aggregate(total=Sum('star'))
        # print(star_sum['total']/len(star))
        #Check if the user is logged in or not
        log_status = Attendance.objects.filter(user_id=request.user,logout_time__isnull=True)
        #Check the total hours of the month
        month = datetime.now().month
        year = datetime.now().year
        hours=Attendance.objects.filter(user_id=request.user,login_time__month=month,login_time__year=year)
        hours_sum = hours.aggregate(total=Sum('hours'))
        orderids=[order.id for order in orders]
        orderlist=OrderList.objects.filter(order_no__in=orderids)
        context = {
            'orders':orders,
            'orderlist':orderlist,
            'orders_today':orders_today,
            'log_status':log_status,
            'hours_sum':hours_sum
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login') 

def menuEditPage(request):
    """Page to edit the menu of the food"""
    if request.user.is_authenticated and request.user.is_staff == True:

        if request.method=="POST":
            if "edit" in request.POST:
                name = request.POST.get('name')
                description = request.POST.get('description')
                type = request.POST.get('type')
                quantity = request.POST.get('quantity')
                status = request.POST.get('status')
                id= request.POST.get('id')
                menuupdate= Menu.objects.get(id=id)
                menuupdate.name=name
                menuupdate.description=description
                menuupdate.type=type
                menuupdate.quantity=quantity
                menuupdate.status=status
                menuupdate.save()

                return redirect('menuEditPage')
            
            elif "remove" in request.POST:
                id= request.POST.get('id')
                menuupdate= Menu.objects.get(id=id)
                menuupdate.delete()
                return redirect('menuEditPage')
            
            elif "add" in request.POST:
                name = request.POST.get('name')
                description = request.POST.get('description')
                type = request.POST.get('type')
                quantity = request.POST.get('quantity')
                status = request.POST.get('status')
                add=Menu.objects.create(
                    name=name,
                    description=description,
                    type=type,
                    quantity=quantity,
                    status=status
                )
                return redirect('menuEditPage')
        menu= Menu.objects.values()
        context = {
            'menu':menu,
        }
        return render(request, 'menuedit.html',context)
    else:
        return redirect('login') 


def custQueries(request):
    """Page to address customer queries"""
    if request.user.is_authenticated and request.user.is_staff == True:
        if request.method=="POST":
            if "update" in request.POST:
                comments = request.POST.get('comments')
                id= request.POST.get('id')
                queries= CustomerRequest.objects.get(id=id)
                queries.comments=comments
                queries.status=1
                queries.staff_ad=request.user
                queries.save()

                return redirect('custQueries')
        queries= CustomerRequest.objects.filter(status=0)
        context = {
            'queries':queries,
        }
        return render(request, 'queries.html',context)
    else:
        return redirect('login') 
    
def StarPageView(request):
    """Page to display the star of the month"""
    staffs=User.objects.filter(is_staff=True)
    employeedata=[]
    a=best_employee.BestEmployee()
    month = datetime.now().month
    year = datetime.now().year
    for staff in staffs:
        total_hours = Attendance.objects.filter(user_id=staff,login_time__month=month,login_time__year=year).aggregate(total_hours=models.Sum('hours'))['total_hours'] or 0
        total_orders = Orders.objects.filter(staff_no=staff).count()
        if total_orders > 0:
            total_rating = Orders.objects.filter(staff_no=staff).aggregate(total_rating=models.Sum('star'))['total_rating'] or 0
            average_rating = total_rating / total_orders
        else:
            average_rating=0
        employee_data = {
            'name': staff.username,
            'hours_worked': total_hours,
            'rating': average_rating,
            'orders_taken': total_orders
        }
        a.add_employee(employee_data['name'], employee_data['hours_worked'], employee_data['rating'], employee_data['orders_taken'])
    result = a.evaluate()
    res = result['ranking']
    print(res)
    context = {
        "winner": result['best_emp'],
        "ranks" : result['ranking']
    }
    return render(request, 'star_employee.html',context)

def logout_user(request):
    """Function for logging out"""
    print("test")
    logout(request)
    return redirect('login')
