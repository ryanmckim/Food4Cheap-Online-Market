from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from .models import *

from .forms import CartItemForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Login unsuccessful. Username or Password is incorrect")
    context = {'form': form}
    return render(request, "login.html", context)


def signup_view(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/Login')
        else:
            error_text = '<ul style="display:flex;'\
                         'flex-direction:column;list-style-type:none;"'
            for msg_list in form.errors.values():
                for msg in msg_list:
                    error_text += f'<li>{msg}</li>'
            error_text += '</ul>'
            messages.error(request, mark_safe(error_text))
    context = {'form': form, }
    return render(request, "signup.html", context)


def sign_out(request):
    logout(request)
    return redirect('/')


def index(request):
    total_price = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(purchaser=request.user)
        for item in cart_items:
            total_price += item.product.price * item.times_bought
    else:
        cart_items = None
    context = {'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "index.html", context)


def bakedgood_view(request): return category_view(request, 1)


def dairys_view(request): return category_view(request, 2)


def fruits_view(request): return category_view(request, 3)


def meats_view(request): return category_view(request, 4)


def seafoods_view(request): return category_view(request, 5)


def vegetables_view(request): return category_view(request, 6)


def category_view(request, pointer):
    total_price = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(purchaser=request.user)
        for item in cart_items:
            total_price += item.product.price * item.times_bought
    else:
        cart_items = None
    products = Product.objects.filter(category=pointer)
    context = {'products': products,
               'category': Category.objects.get(id=pointer),
               'cart_items': cart_items,
               'total_price': total_price,
               }
    return render(request, "category.html", context)


def bakedgood_product_view(request, product): return product_view(request, product, 1)


def dairys_product_view(request, product): return product_view(request, product, 2)


def fruits_product_view(request, product): return product_view(request, product, 3)


def meats_product_view(request, product): return product_view(request, product, 4)


def seafoods_product_view(request, product): return product_view(request, product, 5)


def vegetables_product_view(request, product): return product_view(request, product, 6)


def product_view(request, product, pointer):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CartItemForm(request.POST)
            new_cart_item = CartItem(product=Product.objects.get(name=product),
                                     times_bought=form['times_bought'].value(),
                                     purchaser=request.user)
            new_cart_item.save()
            return redirect('/')
        else:
            messages.error(request, "Please login to purchase items")

    total_price = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(purchaser=request.user)
        for item in cart_items:
            total_price += item.product.price * item.times_bought
    else:
        cart_items = None
    form = CartItemForm()
    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=pointer),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price,
               }
    return render(request, "product.html", context)


def delete_all_items(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            CartItem.objects.filter(purchaser=request.user).delete()
        return redirect('/')


def account_view(request):
    return render(request, "account.html", {})


def about_view(request):
    return render(request, "about.html", {})
