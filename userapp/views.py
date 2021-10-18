from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                print(user.usertype, '----------------user-type')
                if user is not None:
                    login(request, user)
                    if user.usertype == 1:
                        print("TYPE 1")
                        messages.success(request, 'Logged in successfully')
                        return HttpResponseRedirect(reverse('homepage'))
                    elif user.usertype == 2:
                        print("TYPE 2")
                        messages.success(request, 'Logged in successfully')
                        return HttpResponseRedirect(reverse('homepage'))
                    else:
                        print("login failed")
                        return redirect('login_User')
        else:
            fm = AuthenticationForm()
            context = {
                "fm": fm
            }
        return render(request, 'loginpage.html', context)
    else:
        print("USER ALREADY LOGGED-IN")
        return HttpResponseRedirect(reverse('homepage'))


def homepage(request):
    if request.user.is_authenticated:
        print(request.user)
        print(request.user.usertype)
        if request.user.usertype == 1:
            data = "WELCOME CUSTOMER"
            context = {
                "data": data,
            }
        elif request.user.usertype == 2:
            data = "WELCOME SELLER"
            context = {
                "data": data,
            }
        return render(request, 'homepage.html', context)
    else:
        print("LOGIN FIRST!")
        return redirect('login_User')


def logout_user(request):
    logout(request)
    print("logged out")
    return redirect('login_User')


def orders_view(request):
    if request.user.is_authenticated:
        if request.user.usertype == 1:
            return render(request, 'orders.html')
        else:
            return redirect('page_not_found')
    else:
        print("LOGIN FIRST!")
        return redirect('login_User')


def sales_view(request):
    if request.user.is_authenticated:
        if request.user.usertype == 2:
            return render(request, 'sales.html')
        else:
            return redirect('page_not_found')
    else:
        print("LOGIN FIRST!")
        return redirect('login_User')


def page_not_found(request):
    return render(request, 'page_not_found.html')


def signup_users(request):
    if request.method == "POST":
        fm = CustomUserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("SUCCESS!!")
            fm = CustomUserCreationForm()
            return redirect('login_User')
    else:
        form = CustomUserCreationForm()
        context = {
            "fm": form
        }
    return render(request, 'createuser.html', context)
