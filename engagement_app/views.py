from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from .models import LocationNames
from .models import Engagement
from controls_app.models import Control
from django.shortcuts import get_object_or_404

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class EngagementListView(ListView):
    model = models.Engagement


class EngagementDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_detail.html'


class EngagementCreateView(CreateView):
    fields = ("name","partner","office",'industry')
    model = models.Engagement


class EngagementUpdateView(UpdateView):
    fields = ("name","partner","office",'industry')
    model = models.Engagement

class EngagementDeleteView(DeleteView):
    model = models.Engagement
    success_url = reverse_lazy("engagement_app:engagement_list")

class EngagementLandingView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_landing.html'


#Location views
class EngagementMainLocationDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_mainlocation_detail.html'

class EngagementTypeLocationDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_typelocation_detail.html'

class LocationLandingView(DetailView):
    model = models.Engagement
    template_name = 'location_app/location_landing.html'
#location Tree
class LocationTreeUpdateView(UpdateView):
    fields = ('mainlocation_name','subonelocation_name','subtwolocation_name','subthreelocation_name')
    model = models.LocationNames


class LocationTreeCreateView(CreateView):
    fields = ('engagement','mainlocation_name','subonelocation_name','subtwolocation_name','subthreelocation_name')
    model = models.LocationNames

    def get_initial(self):
        engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':engagement}


#Inventory Views
class EngagementInventoryClassDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_inventoryclass_detail.html'


class InventoryLandingView(DetailView):
    model = models.Engagement
    template_name = 'inventory_app/inventory_landing.html'

#count views
class CountLandingView(DetailView):
    model = models.Engagement
    template_name = 'count_app/count_landing.html'

class EngagementCountDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_count_detail.html'


#control views
class ControlLandingView(DetailView):
    model = models.Engagement
    template_name = 'controls_app/control_landing.html'

class EngagementControlDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_control_detail.html'




    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        control_types=Control.objects.all().filter(engagement='2').order_by('control_type').distinct('control_type')
        context['control_types'] = control_types
        context['controls_in_controltypes'] = Control.objects.all().filter(control_type='ITDM Control')
        return context

#control views
class ITLandingView(DetailView):
    model = models.Engagement
    template_name = 'it_app/it_landing.html'

class EngagementITDetailView(DetailView):
    model = models.Engagement
    template_name = 'engagement_app/engagement_it_detail.html'
