from django.contrib import admin

from .models import (
    Supplier,
    Customer,
    Item,
    Drop,
    JobCard,
    Order,
    Delivery
)

admin.site.site_title='AFLink Advertising'
admin.site.site_header='AFLink-Dashboard '

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item)
admin.site.register(Drop)
admin.site.register(JobCard)
admin.site.register(Order)
admin.site.register(Delivery)