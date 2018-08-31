from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
# Create your models here.
class Application(models.Model):
    engagement = models.ForeignKey(Engagement,related_name='control', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','engagement')
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("it_app:control_detail",kwargs={'pk':self.pk})

class Report(models.Model):
    application = models.ForeignKey(Application,related_name='report', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False, default='')
    it_risk_1 = models.TextField(null=True, blank=False, default='')
    it_risk_2 = models.TextField(null=True, blank=False, default='')
    it_risk_3 = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','application')
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("it_app:report_detail",kwargs={'pk':self.pk})
