
# from urllib import request
from django.db import models
# from django.conf import settings
# from django.contrib.sessions.models import Session
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.signals import user_logged_in, user_logged_out

class User(AbstractUser):
    email=models.CharField(max_length=250,blank=True,unique=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_employee=models.BooleanField(default=False)
    is_finance=models.BooleanField(default=False)
    is_general_manager=models.BooleanField(default=False)
    is_logistic=models.BooleanField(default=False)
    USERNAME_FIELD='username'



# class UserSession(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
#     session=models.ForeignKey(Session,on_delete=models.PROTECT)
#     def user_logged_in_handle(sender,request,user,**kwargs):
#         UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)
#     user_logged_in.connect(user_logged_in_handle)

#     def user_logged_out_handle(sender,request,user,**kwargs):
#         UserSession.objects.get_or_create(user=user,session_id=request.session.session_key)

#     user_logged_out.connect(user_logged_out_handle)

    # def user_login_failed_handle(sender,user,credential,**kwargs):
    #     UserSession.objects.get_or_create(user=user,sesion_id=credential.session.session_key)
    # user_login_failed.connect(user_login_failed,request)

    # def delete_user_session(user):
    #     user_sessions=UserSession.objects.filter(user=user)
    #     for user_session in user_sessions:
    #         user_session.session.delete()