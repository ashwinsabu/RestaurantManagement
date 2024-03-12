from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse

# Create your views here.
def IndexPageView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userid = request.POST.get('userid')
            try:
                order=Orders.objects.exclude(user_no=userid,status=5).get(user_no=userid)
                return redirect('food_status',order.id)
            except:
                return redirect('index')
        specials=Menu.objects.filter(status=1)
        context = {
            'specials':specials,
        }
        return render(request, 'users/index.html',context)
    else:
        return redirect('login') 
    # if request.user.is_staff == False:
    #     return render(request, 'users/tables.html')
    # return render(request, 'users/index.html')



def TablePageView(request):
    if request.user.is_authenticated:
        order=Orders.objects.exclude(user_no=request.user.id,status=5).filter(user_no=request.user.id)
        if(order):
            return redirect('food_status',order.id)
        tables = Table.objects.all().values()
        context = {
        'tables': tables,
        }
        return render(request, 'users/tables.html',context)
    else:
        return redirect('login') 

def menuPageView(request, id):
    if request.user.is_authenticated:
        cartList=[]
        if 'cart' in request.session:
            cartid=request.session['cart']
            # print(cartid)
            cartList=Menu.objects.filter(id__in=cartid)
        if request.method == 'POST':
            if 'addcart' in request.POST:
                # print(request.POST)
                menuid = request.POST.get('menu_id')
                menuitem = Menu.objects.get(id=menuid)
                cart = request.session.get('cart', [])
                cart.append(menuitem.id)
                request.session['cart'] = cart
                # print(request.session['cart'])
                return redirect(reverse('menu', args=[id]))
            
            elif 'submitorder' in request.POST:
                cart = request.session.get('cart', [])
                # if len(cart)==0:
                #     print("NOTHING IN CART")
                
                table = Table.objects.get(id=id)
                reserve = User.objects.get(id=1)
                currentuser = request.user
                order = Orders.objects.create(
                        staff_no= reserve,
                        user_no= currentuser,
                        table_no=table,
                        status=1
                    )
                # print(order.id)
                for items in cart:
                    quantity=cart.count(items)
                    if(quantity==0):
                        continue
                    carts=[]
                    carts=[value for value in cart if value != items]
                    print(carts)
                    cart=carts
                    menuitem = Menu.objects.get(id=items)
                    orderlist = OrderList.objects.create(
                        menu_no=menuitem,
                        order_no=order,
                        quantity=quantity
                    )
                # OrderList.objects.filter(order_no=None).update(order_no=order)
                request.session.pop('cart', None)
                return redirect('food_status',order.id)

        menu = Menu.objects.all().values()

        context = {'menu': menu,
                   'cartList':cartList}
        # print(cartList)
        return render(request, 'users/menu.html', context)
    else:
        return redirect('login') 


def stausfoodPageView(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            # print(request.method)
            if "staffcall" in request.POST:
                details=Orders.objects.get(id=id)
                details.status=4
                details.save()
                return redirect('food_status',id)
            elif "billrequest" in request.POST:
                details=Orders.objects.get(id=id)
                details.status=5
                details.save()
                return redirect('index')

        details=Orders.objects.get(id=id)
        # print(details.status)
        context = {
        'details': details,
    }
        return render(request, 'users/food_status.html',context)
    else:
        return redirect('login')

# def siginPageView(request):
#     return render(request, 'users/signin.html')

def contactPageView(request):
    if request.user.is_authenticated:
        if(request.method=='POST'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            orderlist = CustomerRequest.objects.create(
                        name=name,
                        email=email,
                        message=message,
                        status=0
                    )
            return redirect('index')


        return render(request, 'users/contact.html')
    else:
        return redirect('login')

def AboutPageView(request):
    return render(request, 'users/about.html')

