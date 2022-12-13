from django.db import models
from users.models import User

class ApprovalModel(models.Model):
    verified_by=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Verified_by',db_index=True)
    authorized_by=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Verified_by',db_index=True)
    approved_by=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Verified_by',db_index=True)

    def __str__(self):
        return str(self.verified_by)
    @property
    def set_can_verify(self):
        user=User.objects.get(id=id)
        if user.is_logistic==user.is_authenticated and user.is_staff:
            self.verified_by(user)
            self.authorized_by
            return user
        
        if user.is_general_manager==user.is_authenticated and user.is_superuser:
            self.approved_by(user)
            self.authorized_by
            self.verified_by
            return user

        if user.is_finance== user.is_authenticated and user.is_staff:
            self.verified_by
            self.authorized_by
            self.approved_by
            return user

        else:
            raise ValueError('Employees has no right to perform this actionsß')

    
class ApprovalStatus(models.Model):
    pending=models.BooleanField(max_length=7,default='Pending',editable=False)
    reviewing=models.BooleanField(max_length=7,default='Rewiewing',editable=False)
    approved=models.BooleanField(max_length=7,default='Approved',editable=False)
    rejected=models.BooleanField(max_length=7,default='Rejected',editable=False)
    received=models.BooleanField(max_length=7,default='Received',editable=False)

    def __str__(self) -> str:
        return super().__str__(self.pending)

    @property
    def set_can_verify(self):
        user=User.objects.get(id=id)
        if user.is_logistic==user.is_authenticated and user.is_staff:
            self.pending(user)
            self.reviewing
            return user
        
        if user.is_general_manager==user.is_authenticated and user.is_superuser:
            self.pending
            self.reviewing
            self.rejected
            self.approved
            self.received
            return user

        if user.is_finance== user.is_authenticated and user.is_staff:
            self.pending
            self.reviewing
            self.received
            self.rejected
            self.approved
            return user

        else:
            raise ValueError('Employees has no right to perform this actionsß')






