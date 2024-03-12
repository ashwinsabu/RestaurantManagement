from django.shortcuts import render
from restaurant.models import *

# Create your views here.
def StaffIndex(request):
    if request.method=='POST':
        if "prev" in request.POST:
            orderid = request.POST.get('order_id')
            order=Orders.objects.get(id=orderid)
            order.status=order.status-1
            order.save()
        
        elif "next" in request.POST:

            orderid = request.POST.get('order_id')
            order=Orders.objects.get(id=orderid)
            if(order.status<5):
                order.status=order.status+1
            order.save()


    orders=Orders.objects.exclude(staff_no=request.user,status=5).filter(staff_no=request.user)
    orderids=[order.id for order in orders]
    orderlist=OrderList.objects.filter(order_no__in=orderids)
    context = {
        'orders':orders,
        'orderlist':orderlist
    }
    return render(request, 'index.html', context)