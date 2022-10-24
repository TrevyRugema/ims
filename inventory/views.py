from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from aflink.models import Product, Supplier, Customer, Order,Item

@login_required(login_url='login')
def dashboard(request):
    total_item = Item.objects.count()
    total_jobcard = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_customer = Customer.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'item':total_item,
        'jobcard': total_jobcard,
        'supplier': total_supplier,
        'customer': total_customer,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)