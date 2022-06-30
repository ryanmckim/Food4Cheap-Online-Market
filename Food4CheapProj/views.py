from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import CartItemForm


def index(request):
    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "index.html", context)


def bakedgood_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=1)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 1,
               'category': Category.objects.get(id=1),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def dairys_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=2)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 2,
               'category': Category.objects.get(id=2),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def fruits_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=3)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 3,
               'category': Category.objects.get(id=3),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def meats_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=4)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 4,
               'category': Category.objects.get(id=4),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def seafoods_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=5)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 5,
               'category': Category.objects.get(id=5),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def vegetables_view(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.filter(category=6)
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    context = {'product_type': 6,
               'category': Category.objects.get(id=6),
               'products': products,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "category.html", context)


def bakedgood_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()

    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    form = CartItemForm()

    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=1),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "product.html", context)


def dairys_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()

    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    form = CartItemForm()

    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=2),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "product.html", context)


def fruits_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()

    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    form = CartItemForm()

    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=3),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "product.html", context)


def meats_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()

    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    form = CartItemForm()

    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=4),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "product.html", context)


def seafoods_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()

    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.times_bought
    form = CartItemForm()

    context = {'product': Product.objects.get(name=product),
               'category': Category.objects.get(id=5),
               'form': form,
               'cart_items': cart_items,
               'total_price': total_price
               }
    return render(request, "product.html", context)


def vegetables_product_view(request, product):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        new_cart_item = CartItem()
        new_cart_item.product = Product.objects.get(name=product)
        new_cart_item.times_bought = form['times_bought'].value()
        new_cart_item.save()
        return redirect('/')
    else:
        cart_items = CartItem.objects.all()
        total_price = 0
        for item in cart_items:
            total_price += item.product.price * item.times_bought
        form = CartItemForm()

        context = {'product': Product.objects.get(name=product),
                   'category': Category.objects.get(id=6),
                   'form': form,
                   'cart_items': cart_items,
                   'total_price': total_price
                   }
        return render(request, "product.html", context)


def delete_all_items(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
        return redirect('/')
