from django import forms

from users.models import User
from .models import Item, Drop, Product, Order, Delivery


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'phone',
        'data-val': 'true',
        'data-val-required': 'Please enter phone number',
    }))


    
class CustomerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        receivedBy = forms.ModelChoiceField(queryset=User.objects.all())
        fields =['supplier_name','item_name','batch_no','delivery_no','quantity','quantity','unit_cost','date_received','expiry_date','receivedBy','position','document',]
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'item_name'}),
            'batch_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'batch_no'}),
            'delivery_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'delivery_no'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'unit_cost': forms.TextInput(attrs={'class': 'form-control', 'id': 'unit_cost'}),
            'date_received': forms.DateInput(attrs={'class': 'form-control', 'id': 'date_received'}),
            'expiry_date':forms.DateInput(attrs={'class': 'form-control', 'id': 'expiry_date'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'id': 'position'}),
            'document': forms.FileInput(attrs={'class': 'form-control', 'id': 'document'}),
        }
        receivedBy = forms.ModelChoiceField(queryset=User.objects.filter(id=1))

class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['item','quantity','cost','destination','status','requestedby','verifiedby','auhorisedby']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'id': 'item'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'cost': forms.TextInput(attrs={'class': 'form-control', 'id': 'cost'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'id': 'destination'}),
            'status':forms.SelectMultiple(attrs={'class':'form-control','id':'status'})
        }
        requestedby=forms.ModelChoiceField(queryset=User.objects.all())
        verifiedby=forms.ModelChoiceField(queryset=User.objects.all())
        auhorisedby=forms.ModelChoiceField(queryset=User.objects.all())



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'sortno': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sortno'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'product', 'design', 'color', 'customer', 'item_name', 'drop']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'design': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color'}),
            'customer': forms.Select(attrs={'class': 'form-control', 'id': 'customer'}),
            'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
            'drop': forms.Select(attrs={'class': 'form-control', 'id': 'drop'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
        }
