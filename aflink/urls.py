from django.urls import path

from .views import (
    create_supplier,
    create_customer,
    create_item, 
    create_drop,
    create_product,
    create_order,
    create_delivery,
    update_item,


    SupplierListView,
    CustomerListView,
    ItemListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-customer/', create_customer, name='create-customer'),
    path('create-item/', create_item, name='create-item'),
    path('update/<int:item_id>',update_item,name='update-item'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('customer-list/', CustomerListView.as_view(), name='customer-list'),
    path('item-list/', ItemListView.as_view(), name='item-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),

   
]