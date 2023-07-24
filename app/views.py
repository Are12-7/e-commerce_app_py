from django.shortcuts import render, redirect
from . models import Product, User, Cart, Orders
from . forms import RegistrationForm, UserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import stripe
from django.conf import settings
from django.views import View




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
            return redirect('home') 
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

#  ABOUT
def about(req):
    return render(req, "app/about.html")


# CONTACT
def contact(req):
    form = ContactForm()
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('success-message') 
        else:
            messages.warning(req, 'Invalid Input Data')
    return render(req, 'app/contact.html', locals())


# MESSAGE RECEIVED 
def contactMessage(request):
    return render(request, 'app/success_message.html')

# CATEGORY 
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


# ADD TO CART
@login_required(login_url='login')
def addToCart(req):
    user = req.user
    product_id= req.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


# SHOW CART
@login_required(login_url='login')
def showCart(req):
    user = req.user
    cart = Cart.objects.filter(user=user)
    subtotal = 0
    tax = 0
    shipping_price = 0
    for prod in cart:
        total_price = round((prod.quantity * prod.product.discounted_price),2)
        subtotal = round((subtotal + total_price),2)
        shipping_price = 6.99
        tax = round((subtotal + shipping_price) * (0.13),2)
    final_price = round((subtotal + shipping_price + tax),2)
    return render(req,'app/add_to_cart.html', locals())

# PLUS BUTTON
@login_required(login_url='login')
def plusCart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        subtotal = 0
        for prod in cart:
            total_price = round((prod.quantity * prod.product.discounted_price),2)
            subtotal = round((subtotal + total_price),2)
            shipping_price = 6.99
            tax = round((subtotal + shipping_price) * (0.13),2)
        final_price = round((subtotal + shipping_price + tax),2)
        data = {
            'quantity': c.quantity,
            'subtotal': subtotal,
            'tax':tax,
            'final_price': final_price
        }
        return JsonResponse(data)

# MINUS BUTTON 
@login_required(login_url='login')
def minusCart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        subtotal = 0
        for prod in cart:
            total_price = round((prod.quantity * prod.product.discounted_price),2)
            subtotal = round((subtotal + total_price),2)
            shipping_price = 6.99
            tax = round((subtotal + shipping_price) * (0.13),2)
        final_price = round((subtotal + shipping_price + tax),2)
        data = {
            'quantity': c.quantity,
            'subtotal': subtotal,
            'tax':tax,
            'final_price': final_price
        }
        return JsonResponse(data)       

# REMOVE BUTTON
@login_required(login_url='login')
def removeCart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        subtotal = 0
        for prod in cart:
            total_price = round((prod.quantity * prod.product.discounted_price),2)
            subtotal = round((subtotal + total_price),2)
            shipping_price = 6.99
            tax = round((subtotal + shipping_price) * (0.13),2)
        final_price = round((subtotal + shipping_price + tax),2)
        data = {
            'quantity': c.quantity,
            'subtotal': subtotal,
            'tax':tax,
            'final_price': final_price
        }
        return JsonResponse(data)       


stripe.api_key = settings.STRIPE_SECRET_KEY
# CHECKOUT
@login_required(login_url='login')
def checkout_session(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    checkout_items = []
    cart_total = 0
    for item in cart_items:
        cart_total += item.product.discounted_price * item.quantity
        shipping_cost = 6.99
        tax_rate = round(((cart_total +shipping_cost)*0.13),2)
        total_amount = round(cart_total + shipping_cost + tax_rate, 2)

        checkout_item = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': round((total_amount / item.quantity)*100),
                'product_data': {
                    'name': item.product.product_title,
                },
            },
            'quantity': item.quantity,
        }
        checkout_items.append(checkout_item)
        
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=checkout_items,
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url= 'http://localhost:8000/cancel',
        )
        
        # Save checkout session details to the database
        orders = Orders.objects.create(
            session_id=checkout_session.id,
            product_title=item.product.product_title,
            quantity=item.quantity,
            cart_total=cart_total,
            total_amount=total_amount,
            shipping_cost=shipping_cost,
            tax_rate=tax_rate
        )

        return redirect(checkout_session.url, code=303)

    return render(request, "app/checkout.html", locals())


def SuccessfulPayment(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    cart.delete()
    return render(request, 'app/success.html')


def CancelPayment(request):
    return render(request, 'app/cancel.html')


# ORDERS
def OrdersDetail(request):
    orders = Orders.objects.all()
    return render(request, 'app/orders.html', locals())


    






