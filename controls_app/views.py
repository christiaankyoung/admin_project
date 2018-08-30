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
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
# Create your views here.


class ControlDetailView(DetailView):
    model = models.Control
    template_name = 'control_app/control_detail.html'

    #classes = MainLocation.engagement.inventoryclass.all()

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #context['classes'] = classes
        #return context

class ControlCreateView(CreateView):
    model = models.Control
    fields = ('ref','engagement','frequency','control_type','configurable')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context



class ControlUpdateView(UpdateView):
    fields = ("name","engagement")
    model = models.Control

class ControlDeleteView(DeleteView):
    model = models.Control

    def get_success_url(self):
        engagement = get_object_or_404(models.InvCount, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()
