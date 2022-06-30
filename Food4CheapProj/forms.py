from django.forms import ModelForm
from .models import CartItem
from .models import Product
from django.utils.translation import gettext_lazy as _


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ('times_bought',)
        labels = {
            'times_bought': _('Quantity')
        }

