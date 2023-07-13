from django.shortcuts import render, redirect
from . models import Product, User
from . forms import RegistrationForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# REGISTER
def registerPage(req):
    form = RegistrationForm()
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(req, user)
            return redirect('home') # CHANGE TO LOGIN
        else:
            messages.warning(req, 'Invalid Input Data')
            
    return render(req, 'app/register.html', locals())


# LOGIN
def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if user exist
        try:
            user = User.objects.get(email=email)
        except:
            print(email, password)

        # Authenticating username and password
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') #CHANGE TO PROFILE
        else:
            # Does not exist
            messages.error(request, 'Incorrect username or password')

    return render(request, 'app/login.html', locals())


# LOGOUT
def logoutUser(request):
    logout(request)
    return redirect('home')


# PROFILE PAGE
def profilePage(request, id):
    user = User.objects.get(id=id)
    return render(request, 'app/profile.html', locals())


# UPDATE USER/PROFILE
@login_required(login_url='login')
def updateProfile(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', id=user.id)
        else:
            return HttpResponse('Username cannot contain spaces')

    context = {'form': form}
    return render(request, 'app/edit_profile.html', context)


# HOME
def home(req):
    return render(req, "app/home.html")


def category(req, val):
    product = Product.objects.filter(category=val)
    product_title = Product.objects.filter(
        category=val).values('product_title')
    return render(req, "app/category.html", locals())


# CATEGORY FILTER BY TITLE
def categoryTitle(req, val):
    product = Product.objects.filter(product_title=val)
    product_title = Product.objects.filter(
        category=product[0].category).values('product_title')
    return render(req, "app/category.html", locals())

# PRODUCT INFORMATION


def productDetail(req, pk):
    product = Product.objects.get(pk=pk)

    return render(req, "app/product.html", locals())

#  ABOUT


def about(req):
    return render(req, "app/about.html")


# CONTACT
def contact(req):
    return render(req, "app/contact.html")
