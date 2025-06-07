from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages     

from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Book, Users

# Create your views here.

#Registration Validations
def register(request):
        User = get_user_model()
        if request.method == 'POST':
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            cpassword = request.POST["cpassword"]
            if password != cpassword:
                messages.info(request, "Password not match")
                return redirect('/register')
            else:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Taken")
                    return redirect("/register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Taken")
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('/')
        else:
            return render(request, "register.html")
        
#Login Authentication
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("/")
    else:
         return render(request, "index.html")

#logout Authenticate
def log_out(request):
    logout(request)
    return redirect('/')


#Password Reset Authentication
def passreset(request):
    return render(request, 'reset.html')

def main_page(request):
    products = Product.objects.all()
    return render(request, "main_page.html", {'products': products})

@login_required
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def upload(request):
    category_choices = Product._meta.get_field('category').choices
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES.get("upload")
        category = request.POST.get("category")
        stock = request.POST.get("stock") 
        valid_category = dict(category_choices).keys()
        if category in valid_category:
            products = Product.objects.create(
            name=name, 
            description=description, 
            price=price, 
            image=image, 
            category=category,
            stock=stock,
            user=request.user
            )
            Book.objects.create(name=name, user=request.user, products=products)
    
    return render(request, "upload.html", {"category_choices": category_choices})

