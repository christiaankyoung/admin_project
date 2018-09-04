from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from controls_app.models import Control
from location_app.models import MainLocation



# Create your models here.
class Application(models.Model):
    engagement = models.ForeignKey(Engagement,related_name='application', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','engagement')
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("it_app:application_detail",kwargs={'pk':self.pk})

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

class ApplicationControlInfo(models.Model):
    application = models.ForeignKey(Application,related_name='applicationcontrolinfo', on_delete=models.CASCADE, blank=True)
    control = models.ForeignKey(Control,related_name='applicationcontrolinfo', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('application','control')

    def __str__(self):
        return '%s (%s)' % (self.application, self.control)

    def get_absolute_url(self):
        return reverse("it_app:control_detail",kwargs={'pk':self.control.id})


class ReportControlInfo(models.Model):
    report = models.ForeignKey(Report,related_name='reportcontrolinfo', on_delete=models.CASCADE, blank=True)
    control = models.ForeignKey(Control,related_name='reportcontrolinfo', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('report','control')

    def __str__(self):
        return '%s (%s)' % (self.report, self.control)

    def get_absolute_url(self):
        return reverse("it_app:control_detail",kwargs={'pk':self.control.id})

class MainLocationApplication(models.Model):
    application = models.ForeignKey(Application,related_name='mainlocationapplication', on_delete=models.CASCADE, blank=True)
    mainlocation = models.ForeignKey(MainLocation,related_name='mainlocationapplication', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('application','mainlocation')

    def __str__(self):
        return '%s (%s)' % (self.application, self.mainlocation)

    def get_absolute_url(self):
        return reverse("it_app:application_detail",kwargs={'pk':self.application.id})
