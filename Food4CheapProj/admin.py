from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)


class CartItemInline(admin.TabularInline):
    model = CartItem


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]


class UserAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
