from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryClass
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
# Create your views here.


class InventoryClassListView(ListView):
    model = models.InventoryClass


class InventoryClassDetailView(DetailView):
    model = models.InventoryClass
    template_name = 'inventory_app/inventoryclass_detail.html'


class InventoryClassCreateView(CreateView):
    model = models.InventoryClass
    fields = ('classification','engagement')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context

class InventoryClassUpdateView(UpdateView):
    fields = ("classification","engagement")
    model = models.InventoryClass

class InventoryClassDeleteView(DeleteView):
    model = models.InventoryClass

    def get_success_url(self):
        engagement = get_object_or_404(models.InventoryClass, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()
#Inventory type views

class InventoryTypeDetailView(DetailView):
    model = models.InventoryType
    template_name = 'inventory_app/inventorytype/inventorytype_detail.html'

class InventoryTypeCreateView(CreateView):
    model = models.InventoryType
    fields = ('classification','name')
    template_name = 'inventory_app/inventorytype/inventorytype_form.html'

    def get_initial(self):
        self.classification = get_object_or_404(InventoryClass, id=self.kwargs.get('pk'))
        return {'classification':self.classification}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['inventoryclass_name'] = self.classification.classification
        context['inventoryclass_id'] = self.classification.id
        return context

class InventoryTypeUpdateView(UpdateView):
    fields = ("classification","name")
    model = models.InventoryType
    template_name = 'inventory_app/inventorytype/inventorytype_form.html'

class InventoryTypeDeleteView(DeleteView):
    model = models.InventoryType
    template_name = 'inventory_app/inventorytype/inventorytype_confirm_delete.html'

    def get_success_url(self):
        classification = get_object_or_404(models.InventoryType, id=self.kwargs.get('pk')).classification
        return classification.get_absolute_url()
#Inventory Type to Main Location view
class InventoryTypeMainLocationForm(ModelForm):

    class Meta:
        model = models.InventoryTypeMainLocation
        fields = ('mainlocation','type','balance')

    def __init__ (self,*args,**kwargs):
        mainlocation= kwargs.pop('mainlocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        classes = mainlocation.engagement.inventoryclass.all()
        types = []
        for c in classes:
            types.extend(c.inventorytype.all())
        queryset=models.InventoryType.objects.filter(pk__in=[i.id for i in types])
        self.fields['type'].queryset = queryset

class InventoryTypeMainLocationCreateView(CreateView):
    model = models.InventoryTypeMainLocation
    template_name = 'inventory_app\inventorytypemainlocation\inventorytypemainlocation_form.html'
    form_class= InventoryTypeMainLocationForm

    def get_initial(self):
        self.mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_form_kwargs(self):
        kwargs = super(InventoryTypeMainLocationCreateView,self).get_form_kwargs()
        mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        kwargs['mainlocation']=mainlocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['mainlocation_id'] = self.mainlocation.id
        return context

class InventoryTypeMainLocationDeleteView(DeleteView):
    model = models.InventoryTypeMainLocation
    template_name = 'inventory_app/inventorytypemainlocation/inventorytypemainlocation_confirm_delete.html'

    def get_success_url(self):
        mainlocation = get_object_or_404(models.InventoryTypeMainLocation, id=self.kwargs.get('pk')).mainlocation
        return mainlocation.get_absolute_url()

#subone location to inventory type
class InventoryTypeSubOneLocationForm(ModelForm):

    class Meta:
        model = models.InventoryTypeSubOneLocation
        fields = ('subonelocation','type','balance')

    def __init__ (self,*args,**kwargs):
        subonelocation= kwargs.pop('subonelocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        classes = subonelocation.mainlocation.engagement.inventoryclass.all()
        types = []
        for c in classes:
            types.extend(c.inventorytype.all())
        queryset=models.InventoryType.objects.filter(pk__in=[i.id for i in types])
        self.fields['type'].queryset = queryset

class InventoryTypeSubOneLocationCreateView(CreateView):
    model = models.InventoryTypeSubOneLocation
    template_name = 'inventory_app\inventorytypesubonelocation\inventorytypesubonelocation_form.html'
    form_class= InventoryTypeSubOneLocationForm

    def get_initial(self):
        subonelocation = get_object_or_404(SubOneLocation, id=self.kwargs.get('pk'))
        return {'subonelocation':subonelocation}

    def get_form_kwargs(self):
        kwargs = super(InventoryTypeSubOneLocationCreateView,self).get_form_kwargs()
        subonelocation = get_object_or_404(SubOneLocation, id=self.kwargs.get('pk'))
        kwargs['subonelocation']=subonelocation
        return kwargs
