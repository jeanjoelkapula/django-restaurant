from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.urls import reverse
from .models import *
import json

# Create your views here.
def index(request):
    context = {
        "user":request.user,
        "menu_items": MenuItem.objects.all()
    }
    return render(request, "pinochios/index.html", context)

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            previous_page = request.POST['previous_page']
        except KeyError:
            return render(request, 'pinochios/login.html', {'message':'Invalid credentials'})
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if previous_page == 'None':
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('order'))
        else:
            return render(request, 'pinochios/login.html', {'message':'Invalid credentials'})  
    else:
        return render(request, 'pinochios/login.html', {'message':None})

@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password-confirm']
            email = request.POST['email']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
        except KeyError as e:
            print(e)
            return render(request, 'pinochios/register.html', {'message':'Please complete the form'})
        if password_confirm != password:
            return render(request, 'pinochios/register.html', {'message':'The password did not match'})

        user = User.objects.filter(username=username).exists()
        if user:
            return render(request, 'pinochios/register.html', {'message':'The username is already taken'})
        else:
            user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'pinochios/register.html', {'message': None})

def logout_view(request):
    logout(request)
    return render(request, 'pinochios/login.html', {'message': None})

@require_http_methods(['GET', 'POST'])
def order_view(request):
    if request.method == 'POST':
        menu_item = request.POST['menu_item']
        menu_options = MenuOptionAddOn.objects
    else: 
        if not request.user.is_authenticated:
            return render(request, 'pinochios/login.html', {'previous_page':'order', 'message':None})
        else:
            menu = MenuItem.objects.all()
            menu_serialized = Helper.get_menu_serialized(menu)
            context = {
                "menu": menu_serialized,
                "menu_json": json.dumps(menu_serialized)
            }
            return render(request, 'pinochios/order.html', context)

@require_http_methods(['GET', 'POST'])
def cart_view(request):
    if request.method == 'POST':
        pass
    else:
        return(render(request, 'pinochios/cart.html'))

