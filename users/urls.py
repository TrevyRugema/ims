from django.urls import path
from  users import views as user_view
from django.contrib.auth import views as auth
from .views import login_page, logout_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/',user_view.register,name='register')
]