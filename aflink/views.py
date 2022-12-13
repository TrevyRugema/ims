from django.urls import reverse_lazy
from django.shortcuts import (render, redirect, get_object_or_404,HttpResponseRedirect)
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import *
from .forms import *

class JobCardList(ListView):
    model=JobCard
    template_name='aflink/jobcard_list.html'

    def get_queryset(self):
        self.modified_at=get_object_or_404(JobCard,name=self.kwargs('modified_at'))
        return JobCard.objects.filter(modified_at=self.request.user)
    
    def get_context_data(self,**kwargs):
       context= super().get_context_data(**kwargs)
       context['modified_at']=self.request.user
       return context

class JobCardDetailView(DetailView):
    model=JobCard
    success_url=reverse_lazy('jobcard-list')
    context_object_name='job'

    def jobcard_detail(request,id):
        context={}
        context['data']=JobCard.objects.get(id=id)
        return render(request,'aflink/jobcard_detail.html',context)

class JobCardCreate(CreateView):
    model=JobCard
    # fields=['job_type','order_number','date','customer','contact','job_descritpion']
    form_class=JobCardForm
    success_url=reverse_lazy('jobcard-list')
    context_object_name='job'
class JobcardUpdate(UpdateView):
    model=JobCard
    fields=['job_type','order_number','create_at','customer','contact','job_descritpion']
    success_url=reverse_lazy('jobcard-list')
    context_object_name='job'
class JobCardDelete(DeleteView):
    model=JobCard
    success_url=reverse_lazy('jobcard-list')
    context_object_name='job'

# Item Receiving

class ItemList(ListView):
    model=Item
    
class ItemDetailView(DetailView):
    queryset=JobCard.objects.all()
    success_url=reverse_lazy('item-list')
    context_object_name='item'
    template_name='aflink/item_detail.html'

    def get_object(self):
        obj=super().get_object
        obj.receivedBy=self.request.user
        obj.save()
        return obj

class ItemCreate(CreateView):
    model=Item
    fields =['supplier_name','item_name','batch_no','delivery_no','quantity','quantity','unit_cost','date_received','expiry_date','receivedBy','position','document',]
    success_url=reverse_lazy('item-list')
    context_object_name='item'

class ItemUpdate(UpdateView):
    model=Item
    fields =['supplier_name','item_name','batch_no','delivery_no','quantity','quantity','unit_cost','date_received','expiry_date','receivedBy','position','document',]
    success_url=reverse_lazy('item-list')
    context_object_name='item'
class ItemDelete(DeleteView):
    model=Item
    success_url=reverse_lazy('item-list')
    context_object_name='item'