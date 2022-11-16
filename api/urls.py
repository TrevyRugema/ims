from django.urls import path
from .views import *

app_name='api'

urlpatterns=[
    path('<int:pk>/create-item',ItemDetail.as_view(),name='create-item'),
    path('<int:pk>/item-list',ItemList.as_view(),name='item-list'),
    path('<int:pk>/',JobCardDetail.as_view(),name='jobcard_detail'),
    path('',JobCardList.as_view(),name='jobcard_list')
]