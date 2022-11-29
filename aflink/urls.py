from django.urls import path
from  .import views 
    
urlpatterns =[

    path('jobcard-list/', views.JobCardList.as_view(), name='jobcard-list'),
   
    path('view/<int:pk>', views.JobCardView.as_view(), name='jobcard_view'),
    path('new-jobcar', views.JobCardCreate.as_view(), name='jobcard_new'),
    path('edit/<int:pk>', views.JobcardUpdate.as_view(), name='jobcard_edit'),
    path('delete/<int:pk>', views.JobCardDelete.as_view(), name='jobcard_delete')
]