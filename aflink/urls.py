from django.urls import path
from  .import views 
    # register_supplier,
    # create_customer,
    # create_item, 
    # create_drop,
    # # create_jobcard,
    # create_order,
    # create_delivery,

    # SupplierListView,
    # CustomerListView,
    # ItemListView,
    # DropListView,
    # JobCardList,
    # OrderListView,
    # DeliveryListView,
    # JobCardView,
    # JobCardCreate,
    # JobcardUpdate,
    # JobCardDelete



urlpatterns =[
    # path('register-supplier/', register_supplier, name='register-supplier'),
    # path('create-customer/', create_customer, name='create-customer'),
    # path('create-item/', create_item, name='create-item'),
    # path('create-drop/', create_drop, name='create-drop'),
    # # path('create-jobcard/', create_jobcard, name='create-jobcard'),
    # path('create-order/', create_order, name='create-order'),
    # path('create-delivery/', create_delivery, name='create-delivery'),

    # path('supplier-list/', views.SupplierListView.as_view(), name='supplier-list'),
    # path('customer-list/', views.CustomerListView.as_view(), name='customer-list'),
    # path('item-list/', views.ItemListView.as_view(), name='item-list'),
    # path('drop-list/', views.DropListView.as_view(), name='drop-list'),
    path('jobcard-list/', views.JobCardList.as_view(), name='jobcard-list'),
    # path('order-list/', views.OrderListView.as_view(), name='order-list'),
    # path('delivery-list/', views.DeliveryListView.as_view(), name='delivery-list'),
    path('view/<int:pk>', views.JobCardView.as_view(), name='jobcard_view'),
    path('new', views.JobCardCreate.as_view(), name='jobcard_new'),
    path('edit/<int:pk>', views.JobcardUpdate.as_view(), name='jobcard_edit'),
    path('delete/<int:pk>', views.JobCardDelete.as_view(), name='jobcard_delete')
]