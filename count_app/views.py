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
from engagement_app.models import LocationNames
from .models import MainLocation
from .models import MainLocationInfo
from .models import SubOneLocation
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
# Create your views here.


class CountDetailView(DetailView):
    model = models.MainLocation
    template_name = 'count_app/count_detail.html'

    #classes = MainLocation.engagement.inventoryclass.all()

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #context['classes'] = classes
        #return context

class CountCreateView(CreateView):
    model = models.InvCount
    fields = ('name','engagement')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.engagement.locationnames.mainlocation_name
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context



class CountUpdateView(UpdateView):
    fields = ("name","engagement")
    model = models.InvCount

class CountDeleteView(DeleteView):
    model = models.InvCount

    def get_success_url(self):
        engagement = get_object_or_404(models.InvCount, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()
