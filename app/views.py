from django.db.models import Count
from django.shortcuts import render
from . models import Product, Profile
from . forms import RegistrationForm, ProfileForm
from django.contrib import messages


# REGISTER
def register(req):
    form = RegistrationForm()
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'User Register Successfully...')
        else:
            messages.warning(req, 'Invalid Input Data')
    return render(req, 'app/register.html', locals())

# PROFILE


def profile(req):
    form = ProfileForm()
    if req.method == 'POST':
        form = ProfileForm(req.POST)
        if form.is_valid():
            user = req.user
            full_name = form.cleaned_data['full_name']
            mobile = form.cleaned_data['mobile']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            province = form.cleaned_data['province']

            obj = Profile(user=user, full_name=full_name, mobile=mobile,
                          city=city, address=address, zipcode=zipcode, province=province)
            obj.save()
            messages.success(req, 'Profile Updated Successfully...')
        else:
            messages.warning(req, 'Invalid Input Data')

    return render(req, 'app/profile.html', locals())


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
