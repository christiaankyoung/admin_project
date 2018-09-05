from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'index.html'

class ConfigurableView(TemplateView):
    template_name = 'bulblinks/configurable.html'
