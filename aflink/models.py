from email.policy import default
from secrets import choice
from django.utils import timezone
from django.db import models
from users.models import User


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


class Drop(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    item=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    cost=models.DecimalField(max_digits=20,decimal_places=0,null=True)
    destination=models.CharField(max_length=255,null=True)
    requestedby=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='requestedby',null=True)
    verifiedby=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='verifiedby',null=True)
    auhorisedby=models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='auhorisedby',null=True)
    status=models.CharField(max_length=100,blank=False,choices=STATUS_CHOICE,null=True)

    def __str__(self):
        return self.item

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name