from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Customer,
    Item,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    SupplierForm,
    CustomerForm,
    ItemForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)

# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            phone=forms.cleaned_data['phone']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_supplier=True)
                Supplier.objects.create(user=user, name=name, address=address,phone=phone)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addSupplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'aflink/supplier_list.html'
    context_object_name = 'supplier'


# customer views
@login_required(login_url='login')
def create_customer(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_customer=True)
                Customer.objects.create(user=user, name=name, address=address)
                return redirect('customer-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addcustomer.html', context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'aflink/customer_list.html'
    context_object_name = 'customer'

  
# Stock Receiving views
@login_required(login_url='login')
def create_item(request):
    forms = ItemForm()
    if request.method == 'POST':
        forms = ItemForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('item-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addItem.html', context)

class ItemListView(ListView):
    model = Item
    template_name = 'aflink/item_list_cp.html'
    context_object_name = 'item'

  #Update the Stock Receiving

def update_item(request, item_id):
    item_id=int(item_id)
    try:
        items=Item.objects.get(id=item_id)

    except Item.DoesNotExist:
        return redirect('addItem')
    item_form=ItemForm(request.POST or None, instance=items)
    if item_form.is_valid():
        item_form.save()
        return redirect('item-list')
    return render(request,'aflink/addItem.html',{'edit_item':item_form})

# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addCategory.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'aflink/category_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addProduct.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'aflink/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            customer = forms.cleaned_data['customer']
            Item = forms.cleaned_data['Item']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                customer=customer,
                Item=Item,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addOrder.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'aflink/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'aflink/addelivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'aflink/delivery_list.html'
    context_object_name = 'delivery'