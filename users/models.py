
# from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    class Types(models.TextChoices):
        EMLOYEE='EMPLOYEE','Employee',
        FINANCE='FINANCE','Finance',
        GM='GM','General Manager',
        LOGISTIC='LOGISTIC','Logistic'
    type=models.CharField(max_length=10,choices=Types.choices,null=True)
    email=models.CharField(max_length=250,blank=True,unique=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_employee=models.BooleanField(default=False)
    is_finance=models.BooleanField(default=False)
    is_general_manager=models.BooleanField(default=False)
    is_logistic=models.BooleanField(default=False)
    USERNAME_FIELD='username'

    def __str__(self):
        return str(self.type)

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def is_active(self):
        return self.is_active
    def is_employee(self):
        return self.is_employee
    def is_finance(self):
        return self.is_finance
    def is_general_manager(self):
        return self.is_general_manager
    def is_logistic(self):
        return self.is_logistic

    def save(self,*args,**kwargs):
        if not self.type or self.type==None:
            self.type==User.Types
        return super().save(*args,**kwargs)