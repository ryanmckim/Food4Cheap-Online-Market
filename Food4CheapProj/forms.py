from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import CartItem
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ('times_bought',)
        labels = {
            'times_bought': _('Quantity')
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('An account with this username is already registered')
        return self.cleaned_data
