from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserSignUpForm,LoginForm

def sign_up(request):
    """User registeration"""
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_staff=False
            user.save()
            return redirect('login')
    elif request.method == "GET":
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
    
def signin(request):
    """User login"""
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            print("Hiii")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff==True:
                login(request, user)
                return redirect('index_staff')
            elif user is not None and user.is_staff==False:
                login(request, user)
                return redirect('index')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'users/signin.html', {'form': form, 'msg': msg})
