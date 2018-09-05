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


class CountDetailView(DetailView):
    model = models.MainLocation
    template_name = 'count_app/count_detail.html'


class CountCreateForm(ModelForm):

    class Meta:
        model = models.InvCount
        fields = ('inventorytypemainlocation','ref','engagement','date','blindcount','control')

    def __init__ (self,*args,**kwargs):
        engagement= kwargs.pop('engagement')
        inventorytypes = []
        super(ModelForm, self).__init__(*args,**kwargs)
        controls = engagement.control.all()
        queryset=models.Control.objects.filter(pk__in=[i.id for i in controls])
        self.fields['control'].queryset = queryset


class CountCreateView(CreateView):
    model = models.InvCount
    form_class= CountCreateForm

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_form_kwargs(self):
        kwargs = super(CountCreateView,self).get_form_kwargs()
        engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        kwargs['engagement']=engagement
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_id'] = self.engagement.id
        context['engagement_name'] = self.engagement.name
        return context


class CountUpdateView(UpdateView):
    fields = ("name","engagement")
    model = models.InvCount

class CountDeleteView(DeleteView):
    model = models.InvCount

    def get_success_url(self):
        engagement = get_object_or_404(models.InvCount, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()
