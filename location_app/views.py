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
from controls_app.models import MainLocationControl
from controls_app.models import SubOneLocationControl
from controls_app.models import Control
from .models import MainLocation
from .models import TypeLocation
from .models import MainLocationInfo
from .models import SubOneLocation
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
# Create your views here.


class MainLocationListView(ListView):
    model = models.MainLocation


class MainLocationDetailView(DetailView):
    model = models.MainLocation
    template_name = 'location_app/mainlocation_detail.html'


class MainLocationCreateView(CreateView):
    model = models.MainLocation
    fields = ("name","engagement","address",'description')

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.engagement.locationnames.mainlocation_name
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context



class MainLocationUpdateView(UpdateView):
    fields = ("name","engagement","address",'description')
    model = models.MainLocation

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('en_pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context


class MainLocationDeleteView(DeleteView):
    model = models.MainLocation

    def get_success_url(self):
        engagement = get_object_or_404(models.MainLocation, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()
#TypeLocation Views

class TypeLocationCreateView(CreateView):
    fields = ("type","engagement",'description')
    model = models.TypeLocation
    template_name = 'location_app/typelocation/typelocation_form.html'

    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_id'] = self.engagement.id
        return context

class TypeLocationDetailView(DetailView):
    model = models.TypeLocation
    template_name = 'location_app/typelocation/typelocation_detail.html'


class TypeLocationUpdateView(UpdateView):
    fields = ("type","engagement",'description')
    model = models.TypeLocation
    template_name = 'location_app/typelocation/typelocation_form.html'


    def get_initial(self):
        self.engagement = get_object_or_404(Engagement, id=self.kwargs.get('en_pk'))
        return {'engagement':self.engagement}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['engagement_name'] = self.engagement.name
        context['engagement_id'] = self.engagement.id
        return context

class TypeLocationDeleteView(DeleteView):
    model = models.TypeLocation
    template_name = 'location_app/typelocation/typelocation_confirm_delete.html'

    def get_success_url(self):
        engagement = get_object_or_404(models.TypeLocation, id=self.kwargs.get('pk')).engagement
        return engagement.get_absolute_url()

#Main Location Info Views
class MainTypeForm(ModelForm):

    class Meta:
        model = models.MainLocationInfo
        fields = ('mainlocation','type')

    def __init__ (self,*args,**kwargs):
        mainlocation= kwargs.pop('mainlocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        types = mainlocation.engagement.typelocation.all()
        queryset=models.TypeLocation.objects.filter(pk__in=[i.id for i in types])
        self.fields['type'].queryset = queryset

class MainTypeCreateView(CreateView):
    model = models.MainLocationInfo
    form_class= MainTypeForm

    def get_initial(self):
        self.mainlocation = get_object_or_404(models.MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_form_kwargs(self):
        kwargs = super(MainTypeCreateView,self).get_form_kwargs()
        mainlocation = get_object_or_404(MainLocation, id=self.kwargs.get('pk'))
        kwargs['mainlocation']=mainlocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['mainlocation_id'] = self.mainlocation.id
        return context

class MainTypeDeleteView(DeleteView):
    model = models.MainLocationInfo

    def get_success_url(self):
        mainlocation = get_object_or_404(models.MainLocationInfo, id=self.kwargs.get('pk')).mainlocation
        return mainlocation.get_absolute_url()

class TypeLocationListView(ListView):
    model = models.TypeLocation


# main Location Detail for engagements
class MainLocationEngagementDetailView(DetailView):
    model = models.MainLocation
    template_name = 'location_app/mainlocation_detail.html'

# Sub One Views
class SubOneLocationCreateView(CreateView):
    model = models.SubOneLocation
    fields = ("name","mainlocation",'description','address')
    template_name = 'location_app/subone/subonelocation_form.html'

    def get_initial(self):
        self.mainlocation = get_object_or_404(models.MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['subonelocation_called'] = self.mainlocation.engagement.locationnames.subonelocation_name
        context['mainlocation_id'] = self.mainlocation.id
        return context

class SubOneLocationDetailView(DetailView):
    model = models.SubOneLocation
    template_name = 'location_app/subone/subonelocation_detail.html'

class SubOneLocationUpdateView(UpdateView):
    model = models.SubOneLocation
    fields = ("name","mainlocation",'description','address')
    template_name = 'location_app/subone/subonelocation_form.html'

    def get_initial(self):
        self.mainlocation = get_object_or_404(models.MainLocation, id=self.kwargs.get('pk'))
        return {'mainlocation':self.mainlocation}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.mainlocation.name
        context['subonelocation_called'] = self.mainlocation.engagement.locationnames.subonelocation_name
        context['mainlocation_id'] = self.mainlocation.id
        return context


class SubOneLocationDeleteView(DeleteView):
    model = models.SubOneLocation
    template_name = 'location_app/subone/subonelocation_confirm_delete.html'

    def get_success_url(self):
        mainlocation = get_object_or_404(models.SubOneLocation, id=self.kwargs.get('pk')).mainlocation
        return mainlocation.get_absolute_url()

#SubOne Location Info Views
class SubOneTypeForm(ModelForm):

    class Meta:
        model = models.SubOneLocationInfo
        fields = ('subonelocation','type')

    def __init__ (self,*args,**kwargs):
        subonelocation= kwargs.pop('subonelocation')
        super(ModelForm, self).__init__(*args,**kwargs)
        types = subonelocation.mainlocation.engagement.typelocation.all()
        queryset=models.TypeLocation.objects.filter(pk__in=[i.id for i in types])
        self.fields['type'].queryset = queryset


class SubOneTypeCreateView(CreateView):
    model = models.SubOneLocationInfo
    form_class= SubOneTypeForm
    template_name = 'location_app/subone/subonelocationinfo_form.html'

    def get_initial(self):
        self.subonelocation = get_object_or_404(models.SubOneLocation, id=self.kwargs.get('pk'))
        return {'subonelocation':self.subonelocation}

    def get_form_kwargs(self):
        kwargs = super(SubOneTypeCreateView,self).get_form_kwargs()
        subonelocation = get_object_or_404(SubOneLocation, id=self.kwargs.get('pk'))
        kwargs['subonelocation']=subonelocation
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_name'] = self.subonelocation.mainlocation.name
        context['subonelocation_name'] = self.subonelocation.name
        context['subonelocation_id'] = self.subonelocation.id
        context['mainlocation_id'] = self.subonelocation.mainlocation.id
        return context

class SubOneTypeDeleteView(DeleteView):
    model = models.SubOneLocationInfo
    template_name = 'location_app/subone/subonelocationinfo_confirm_delete.html'

    def get_success_url(self):
        subonelocation = get_object_or_404(models.SubOneLocationInfo, id=self.kwargs.get('pk')).subonelocation
        return subonelocation.get_absolute_url()
#Sub Two views
class SubTwoLocationCreateView(CreateView):
    fields = ("name","subonelocation")
    model = models.SubTwoLocation
    template_name = 'location_app/subtwo/subtwolocation_form.html'

    def get_initial(self):
        self.subonelocation = get_object_or_404(models.SubOneLocation, id=self.kwargs.get('pk'))
        return {'subonelocation':self.subonelocation}

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['subonelocation_name'] = self.subonelocation.name
        context['subtwolocation_called'] = self.subonelocation.mainlocation.engagement.locationnames.subtwolocation_name
        context['subonelocation_id'] = self.subonelocation.id
        context['mainlocation_id'] = self.subonelocation.mainlocation.id
        return context

class SubTwoLocationDetailView(DetailView):
    model = models.SubTwoLocation
    template_name = 'location_app/subtwo/subtwolocation_detail.html'

class SubTwoLocationUpdateView(UpdateView):
    model = models.SubTwoLocation
    fields = ("name","subonelocation")
    template_name = 'location_app/subtwo/subtwolocation_form.html'

class SubTwoLocationDeleteView(DeleteView):
    model = models.SubTwoLocation
    template_name = 'location_app/subtwo/subtwolocation_confirm_delete.html'

    def get_success_url(self):
        subonelocation = get_object_or_404(models.SubTwoLocation, id=self.kwargs.get('pk')).subonelocation
        return subonelocation.get_absolute_url()

#Control Mainlocation views

class ControlMainLocationForm(ModelForm):

    class Meta:
        model = MainLocationControl
        fields = ('mainlocation','control','description')

    def __init__ (self,*args,**kwargs):
        control= kwargs.pop('control')
        super(ModelForm, self).__init__(*args,**kwargs)
        mainlocations = control.engagement.mainlocation.all()
        queryset=models.MainLocation.objects.filter(pk__in=[i.id for i in mainlocations])
        self.fields['mainlocation'].queryset = queryset

class ControlMainLocationCreateView(CreateView):
    model = MainLocationControl
    template_name = 'controls_app\controlmainlocation\controlmainlocation_form.html'
    form_class= ControlMainLocationForm

    def get_initial(self):
        self.control = get_object_or_404(Control, id=self.kwargs.get('pk'))
        return {'control':self.control}

    def get_form_kwargs(self):
        kwargs = super(ControlMainLocationCreateView,self).get_form_kwargs()
        control = get_object_or_404(Control, id=self.kwargs.get('pk'))
        kwargs['control']=control
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_called'] = self.control.engagement.locationnames.mainlocation_name
        context['control_id'] = self.control.id
        context['control_ref'] = self.control.ref
        return context

#Control Sub Onelocation views

class ControlSubOneLocationForm(ModelForm):

    class Meta:
        model = SubOneLocationControl
        fields = ('subonelocation','control','description')

    def __init__ (self,*args,**kwargs):
        control= kwargs.pop('control')
        subonelocations = []
        super(ModelForm, self).__init__(*args,**kwargs)
        mainlocations = control.engagement.mainlocation.all()
        for sub in mainlocations:
            subonelocations.extend(sub.subonelocation.all())
        queryset=models.SubOneLocation.objects.filter(pk__in=[i.id for i in subonelocations])
        self.fields['subonelocation'].queryset = queryset

class ControlSubOneLocationCreateView(CreateView):
    model = SubOneLocationControl
    template_name = 'controls_app\controlsubonelocation\controlsubonelocation_form.html'
    form_class= ControlSubOneLocationForm

    def get_initial(self):
        self.control = get_object_or_404(Control, id=self.kwargs.get('pk'))
        return {'control':self.control}

    def get_form_kwargs(self):
        kwargs = super(ControlSubOneLocationCreateView,self).get_form_kwargs()
        control = get_object_or_404(Control, id=self.kwargs.get('pk'))
        kwargs['control']=control
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['mainlocation_called'] = self.control.engagement.locationnames.subonelocation_name
        context['control_id'] = self.control.id
        context['control_ref'] = self.control.ref
        return context
#type main associate view
class TypeMainForm(ModelForm):

    class Meta:
        model = models.MainLocationInfo
        fields = ('mainlocation','type')

    def __init__ (self,*args,**kwargs):
        type= kwargs.pop('type')
        super(ModelForm, self).__init__(*args,**kwargs)
        mainlocations = type.engagement.mainlocation.all()
        queryset=models.MainLocation.objects.filter(pk__in=[i.id for i in mainlocations])
        self.fields['mainlocation'].queryset = queryset

class TypeMainCreateView(CreateView):
    model = models.MainLocationInfo
    form_class= TypeMainForm
    template_name = 'location_app\mainlocationtype_form.html'

    def get_initial(self):
        self.type = get_object_or_404(models.TypeLocation, id=self.kwargs.get('pk'))
        return {'type':self.type}

    def get_form_kwargs(self):
        kwargs = super(TypeMainCreateView,self).get_form_kwargs()
        type = get_object_or_404(TypeLocation, id=self.kwargs.get('pk'))
        kwargs['type']=type
        return kwargs

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['typelocation_name'] = self.type.type
        context['typelocation_id'] = self.type.id
        context['mainlocation_called'] = self.type.engagement.locationnames.mainlocation_name
        return context
