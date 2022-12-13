from django.urls import path,re_path
from aflink.views import *
    
urlpatterns =[

    # Job Card Urls
    path('jobcard-list/', JobCardList.as_view(), name='jobcard-list'),
    path('jobcard-view<int:pk>/', JobCardDetailView.as_view(), name='jobcard_view'),
    path('create-jobcard/', JobCardCreate.as_view(), name='jobcard_new'),
    path('update-jobcard/<int:pk>', JobcardUpdate.as_view(), name='jobcard_edit'),
    path('delete-jobcard/<int:pk>', JobCardDelete.as_view(), name='jobcard_delete'),

    # Item Recwiving Urls
    path('item-list/', ItemList.as_view(), name='item-list'),
    path('create-new-item/', ItemCreate.as_view(), name='create-new-item'),
    re_path('<int:item_id>',ItemDetailView.as_view(),name='view_item'),
    path('update-item/<int:pk>/', ItemUpdate.as_view(), name='item-edit'),
    path('delete-item/<int:pk>/', ItemDelete.as_view(), name='item-delete')


]