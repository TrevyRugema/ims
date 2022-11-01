from ast import Del
from django.urls import path

from .views import (
    register_supplier,
    create_customer,
    create_item, 
    create_drop,
    create_jobcard,
    create_order,
    create_delivery,

    SupplierListView,
    CustomerListView,
    ItemListView,
    DropListView,
    JobCardListView,
    OrderListView,
    DeliveryListView,
    ItemUpdate,
    DeleteItem
    
)

urlpatterns =[
    path('register-supplier/', register_supplier, name='register-supplier'),
    path('create-customer/', create_customer, name='create-customer'),
    path('create-item/', create_item, name='create-item'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-jobcard/', create_jobcard, name='create-jobcard'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('customer-list/', CustomerListView.as_view(), name='customer-list'),
    path('item-list/', ItemListView.as_view(), name='item-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('jobcard-list/', JobCardListView.as_view(), name='jobcard-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('update-item/', ItemUpdate.as_view(),name='update-item'),
    path('delete-item/', DeleteItem.as_view(),name='delete-item')
 
]