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
from it_app.models import Application
from location_app.models import MainLocation
from inventory_app.models import InventoryType
from django.shortcuts import get_object_or_404
from django.forms import ModelForm

class ApplicationDetailView(DetailView):
    model = models.Application
    template_name = 'it_app/application_detail.html'

    #classes = MainLocation.engagement.inventoryclass.all()

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #context['classes'] = classes
        #return context

class ApplicationCreateView(CreateView):
    model = models.Application
    fields = ('engagement','name','description')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context



class ApplicationUpdateView(UpdateView):
    fields = ('engagement','name','description')
    model = models.Application

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('en_pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context

class ApplicationDeleteView(DeleteView):
    model = models.Application

    def get_success_url(self):
        engagement = get_object_or_404(models.Application, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()

#report Views
class ReportDetailView(DetailView):
    model = models.Report
    template_name = 'it_app/report/report_detail.html'


class ReportCreateView(CreateView):
    model = models.Report
    fields = ('application','name','description','it_risk_1','it_risk_2','it_risk_3')
    template_name = 'it_app/report/report_form.html'

    def get_initial(self):
        self.application = get_object_or_404(Application, id=self.kwargs.get('pk'))
        return {'application':self.application}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['application_name'] = self.application.name
        context['application_id'] = self.application.id
        return context



class ReportUpdateView(UpdateView):
    fields = ('application','name','description','it_risk_1','it_risk_2','it_risk_3')
    template_name = 'it_app/report/report_form.html'

    model = models.Report

    def get_initial(self):
        self.application = get_object_or_404(Application, id=self.kwargs.get('en_pk'))
        return {'application':self.application}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['application_name'] = self.application.name
        context['application_id'] = self.application.id
        return context

class ReportDeleteView(DeleteView):
    model = models.Report
    template_name = 'it_app/report/report_confirm_delete.html'

    def get_success_url(self):
        application = get_object_or_404(models.Report, id=self.kwargs.get('pk')).application
        return application.get_absolute_url()

class MainLocationApplicationForm(ModelForm):

    class Meta:
        model = models.MainLocationApplication
        fields = ('mainlocation','application','description')

    def __init__ (self,*args,**kwargs):
        mainlocation= kwargs.pop('mainlocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        applications = mainlocation.engagement.application.all()
        queryset=models.Application.objects.filter(pk__in=[i.id for i in applications])
        self.fields['application'].queryset = queryset

class MainLocationApplicationCreateView(CreateView):
    model = models.MainLocationApplication
    template_name = 'it_app\mainlocationapplication\mainlocationapplication_form.html'
    form_class= MainLocationApplicationForm

    def get_initial(self):
        self.mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_form_kwargs(self):
        kwargs = super(MainLocationApplicationCreateView,self).get_form_kwargs()
        mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        kwargs['mainlocation']=mainlocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['mainlocation_id'] = self.mainlocation.id
        return context


class MainLocationApplicationDeleteView(DeleteView):
    model = models.MainLocationApplication
    template_name = 'it_app/mainlocationapplication/mainlocationapplication_confirm_delete.html'

    def get_success_url(self):
        mainlocation = get_object_or_404(models.MainLocationApplication, id=self.kwargs.get('pk')).mainlocation
        return mainlocation.get_absolute_url()

#InventoryType to application
class InventoryTypeApplicationForm(ModelForm):

    class Meta:
        model = models.InventoryTypeApplication
        fields = ('inventorytype','application','description')

    def __init__ (self,*args,**kwargs):
        inventorytype= kwargs.pop('inventorytype')
        super(ModelForm, self).__init__(*args,**kwargs)
        applications = inventorytype.classification.engagement.application.all()
        queryset=models.Application.objects.filter(pk__in=[i.id for i in applications])
        self.fields['application'].queryset = queryset

class InventoryTypeApplicationCreateView(CreateView):
    model = models.InventoryTypeApplication
    template_name = 'it_app\inventorytypeapplication\inventorytypeapplication_form.html'
    form_class= InventoryTypeApplicationForm

    def get_initial(self):
        self.inventorytype = get_object_or_404(InventoryType, id=self.kwargs.get('pk'))
        return {'inventorytype':self.inventorytype}

    def get_form_kwargs(self):
        kwargs = super(InventoryTypeApplicationCreateView,self).get_form_kwargs()
        inventorytype = get_object_or_404(InventoryType, id=self.kwargs.get('pk'))
        kwargs['inventorytype']=inventorytype
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['inventorytype_name'] = self.inventorytype
        context['inventorytype_id'] = self.inventorytype.id
        return context


class InventoryTypeApplicationDeleteView(DeleteView):
    model = models.InventoryTypeApplication
    template_name = 'it_app/inventorytypeapplication/inventorytypeapplication_confirm_delete.html'

    def get_success_url(self):
        inventorytype = get_object_or_404(models.InventoryTypeApplication, id=self.kwargs.get('pk')).inventorytype
        return inventorytype.get_absolute_url()
