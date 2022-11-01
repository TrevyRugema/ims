from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .forms import ItemForm

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

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=('id','item_name','quantity','unit_cost','total_cost','date_received','receivedBy','document')
    list_display_links=['id','item_name','quantity']
    search_fields=['id', 'date_received']
    list_editable=['document']
    list_per_page=5
  

    form=ItemForm

    def export_selected_objects(modeladmin,request,queryset):
        selected=queryset.value_list('pk', flat=True)
        ct=ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect('/export/?ct=%s&ids=%s' %(ct.pk, ','.join(str(pk) for pk in selected), 
        ))

    admin.site.add_action(export_selected_objects,'export_selected')

    
    



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name', 'address', 'created_date']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name', 'address', 'created_date']

@admin.register(Drop)
class DropAdmin(admin.ModelAdmin):
    pass

@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    pass






admin.site.register(Order)
admin.site.register(Delivery)