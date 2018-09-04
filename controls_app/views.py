from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from engagement_app.models import Engagement
from controls_app.models import MainLocationControl
from controls_app.models import Control
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryClass
from inventory_app.models import InventoryType
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
# Create your views here.


class ControlDetailView(DetailView):
    model = models.Control
    template_name = 'controls_app/control_detail.html'

    #classes = MainLocation.engagement.inventoryclass.all()

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #context['classes'] = classes
        #return context

class ControlCreateView(CreateView):
    model = models.Control
    fields = ('ref','name','description','engagement','frequency','control_type','configurable')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context

class ControlUpdateView(UpdateView):
    fields = ('ref','name','description','engagement','frequency','control_type','configurable')
    model = models.Control

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('en_pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context

class ControlDeleteView(DeleteView):
    model = models.Control

    def get_success_url(self):
        engagement = get_object_or_404(models.Control, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()

# Control association with main location view

class MainLocationControlForm(ModelForm):

    class Meta:
        model = models.MainLocationControl
        fields = ('mainlocation','control','description')

    def __init__ (self,*args,**kwargs):
        mainlocation= kwargs.pop('mainlocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        controls = mainlocation.engagement.control.all()
        queryset=models.Control.objects.filter(pk__in=[i.id for i in controls])
        self.fields['control'].queryset = queryset

class MainLocationControlCreateView(CreateView):
    model = models.MainLocationControl
    template_name = 'controls_app\mainlocationcontrol\mainlocationcontrol_form.html'
    form_class= MainLocationControlForm

    def get_initial(self):
        self.mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_form_kwargs(self):
        kwargs = super(MainLocationControlCreateView,self).get_form_kwargs()
        mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        kwargs['mainlocation']=mainlocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['mainlocation_id'] = self.mainlocation.id
        return context


class MainLocationControlDeleteView(DeleteView):
    model = models.MainLocationControl
    template_name = 'controls_app/mainlocationcontrol/mainlocationcontrol_confirm_delete.html'

    def get_success_url(self):
        mainlocation = get_object_or_404(models.MainLocationControl, id=self.kwargs.get('pk')).mainlocation
        return mainlocation.get_absolute_url()

# Control association with sub one location view

class SubOneLocationControlForm(ModelForm):

    class Meta:
        model = models.SubOneLocationControl
        fields = ('subonelocation','control','description')

    def __init__ (self,*args,**kwargs):
        subonelocation= kwargs.pop('subonelocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        controls = subonelocation.mainlocation.engagement.control.all()
        queryset=models.Control.objects.filter(pk__in=[i.id for i in controls])
        self.fields['control'].queryset = queryset

class SubOneLocationControlCreateView(CreateView):
    model = models.SubOneLocationControl
    template_name = 'controls_app\subonelocationcontrol\subonelocationcontrol_form.html'
    form_class= SubOneLocationControlForm

    def get_initial(self):
        self.subonelocation = get_object_or_404(SubOneLocation, id=self.kwargs.get('pk'))
        return {'subonelocation':self.subonelocation}

    def get_form_kwargs(self):
        kwargs = super(SubOneLocationControlCreateView,self).get_form_kwargs()
        self.subonelocation = get_object_or_404(SubOneLocation, id=self.kwargs.get('pk'))
        kwargs['subonelocation']=self.subonelocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.subonelocation.name
        context['mainlocation_id'] = self.subonelocation.mainlocation.id
        context['subonelocation_id'] = self.subonelocation.id
        return context

class SubOneLocationControlDeleteView(DeleteView):
    model = models.SubOneLocationControl
    template_name = 'control_app/subonelocationcontrol/subonelocationcontrol_confirm_delete.html'

    def get_success_url(self):
        subonelocation = get_object_or_404(models.SubOneLocationControl, id=self.kwargs.get('pk')).subonelocation
        return subonelocation.get_absolute_url()

# Control association with class view

class InventoryClassControlForm(ModelForm):

    class Meta:
        model = models.InventoryClassControl
        fields = ('inventoryclass','control','description')

    def __init__ (self,*args,**kwargs):
        inventoryclass= kwargs.pop('inventoryclass')
        super(ModelForm, self).__init__(*args,**kwargs)
        controls = inventoryclass.engagement.control.all()
        queryset=models.Control.objects.filter(pk__in=[i.id for i in controls])
        self.fields['control'].queryset = queryset

class InventoryClassControlCreateView(CreateView):
    model = models.InventoryClassControl
    template_name = 'controls_app\inventoryclasscontrol\inventoryclasscontrol_form.html'
    form_class= InventoryClassControlForm

    def get_initial(self):
        self.inventoryclass = get_object_or_404(InventoryClass, id=self.kwargs.get('pk'))
        return {'inventoryclass':self.inventoryclass}

    def get_form_kwargs(self):
        kwargs = super(InventoryClassControlCreateView,self).get_form_kwargs()
        inventoryclass = get_object_or_404(InventoryClass, id=self.kwargs.get('pk'))
        kwargs['inventoryclass']=inventoryclass
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['inventoryclass_name'] = self.inventoryclass.classification
        context['inventoryclass_id'] = self.inventoryclass.id
        return context


class InventoryClassControlDeleteView(DeleteView):
    model = models.InventoryClassControl
    template_name = 'control_app/inventoryclasscontrol/inventoryclasscontrol_confirm_delete.html'

    def get_success_url(self):
        inventoryclass = get_object_or_404(models.InventoryClassControl, id=self.kwargs.get('pk')).inventoryclass
        return inventoryclass.get_absolute_url()

# Control association with type view

class InventoryTypeControlForm(ModelForm):

    class Meta:
        model = models.InventoryTypeControl
        fields = ('inventorytype','control','description')

    def __init__ (self,*args,**kwargs):
        inventorytype= kwargs.pop('inventorytype')
        super(ModelForm, self).__init__(*args,**kwargs)
        controls = inventorytype.classification.engagement.control.all()
        queryset=models.Control.objects.filter(pk__in=[i.id for i in controls])
        self.fields['control'].queryset = queryset

class InventoryTypeControlCreateView(CreateView):
    model = models.InventoryTypeControl
    template_name = 'controls_app\inventorytypecontrol\inventorytypecontrol_form.html'
    form_class= InventoryTypeControlForm

    def get_initial(self):
        self.inventorytype = get_object_or_404(InventoryType, id=self.kwargs.get('pk'))
        return {'inventorytype':self.inventorytype}

    def get_form_kwargs(self):
        kwargs = super(InventoryTypeControlCreateView,self).get_form_kwargs()
        inventorytype = get_object_or_404(InventoryType, id=self.kwargs.get('pk'))
        kwargs['inventorytype']=inventorytype
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['inventorytype_name'] = self.inventorytype.name
        context['inventorytype_id'] = self.inventorytype.id
        return context


class InventoryTypeControlDeleteView(DeleteView):
    model = models.InventoryTypeControl
    template_name = 'control_app/inventorytypecontrol/inventorytypecontrol_confirm_delete.html'

    def get_success_url(self):
        inventorytype = get_object_or_404(models.InventoryTypeControl, id=self.kwargs.get('pk')).inventorytype
        return inventorytype.get_absolute_url()
