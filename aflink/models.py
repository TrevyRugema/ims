
from django.utils import timezone
from django.db.models import TextChoices
from django.db import models
from users.models import User
from django_fsm import FSMField, transition
from django.utils.translation import gettext_lazy as _

class StatusChoices(TextChoices):
    NEW='NEW',_('New'),
    APPROVED='APPROVED',_('Approved'),
    REJECTED='REJECTED',_('Rejected'),
    RECEIVED='RECEIVED',_('Received')
Approvals=(
    ('Job-Assess','Job-Assess', ),
    ('Finance-Approvals','Finance-Approvals'),
    ('Logistics-Approvals','Logistics-Approvals'),
    ('GM-Approvals','GM-Approvals'),
    ('Issuing-Materials','Issuing-Materials')
)
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Item(models.Model):
    class ItemObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()
    supplier_name=models.CharField("Supplier Name", max_length=150,blank=False,null=True)
    item_name=models.CharField("Item Name", max_length=150,blank=False)
    delivery_no=models.CharField("Delivery Number", max_length=100,blank=False)
    batch_no=models.CharField("Batch Number",max_length=100,blank=False)
    quantity=models.FloatField("Quantity")
    unit_cost=models.FloatField("Unit Cost")
    date_received=models.DateTimeField(default=timezone.now)
    expiry_date=models.DateTimeField(default=timezone.now)
    receivedBy=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    position=models.CharField(max_length=100)
    document=models.FileField(upload_to='media',blank=True)
    objects=models.Manager() #Defauly Manager
    itemobjects=ItemObjects() #Custom Manager

    def __str__(self):
        return self.item_name

    @property
    def total_cost(self):
        total=self.quantity * self.unit_cost
        return total
    class Meta:
        db_table="Item Receiving"
       
class Requisition(models.Model):
    item=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    cost=models.DecimalField(max_digits=20,decimal_places=0,null=True)
    destination=models.CharField(max_length=255,null=True)
    requestedby=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='requestedby',null=True)
    verifiedby=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='verifiedby',null=True)
    auhorisedby=models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='auhorisedby',null=True)

    def __str__(self):
        return self.item

class JobCard(models.Model):
    job_type=models.CharField("Job Type", max_length=50,null=True) #  here ithis field will have a choice 
    order_number=models.CharField("Order Number", max_length=50,null=True)
    date=models.DateField(null=True)
    customer=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=13,null=True)
    job_descritpion=models.TextField("Job Description",null=True)
    def __str__(self):
        return self.job_type

class JobCardFLow(models.Model):
    jobcard=models.ForeignKey(JobCard,on_delete=models.PROTECT)
    state=FSMField(default='new')
@transition(field='state',source=['Job-Assess'],target=Approvals)

# class Material(models.Model):
#     material_requested=models.CharField("Material Requested", max_length=100)
#     Description=models.TextField()
#     quantity=models.IntegerField()
#     width=models.DecimalField(max_digits=10,decimal_places=0)
#     height=models.DecimalField(max_digits=20,decimal_places=0)
#     jobcard=models.ForeignKey(JobCard, on_delete=models.PROTECT)

#     def __str__(self):
#         return self.material_requested


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    jobcard = models.ForeignKey(JobCard, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Requisition, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.jobcard.name

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name