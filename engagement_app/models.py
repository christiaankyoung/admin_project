from django.db import models
from django.urls import reverse
# Create your models here.
class Engagement(models.Model):
    name = models.CharField(max_length=56, unique=True)
    partner = models.CharField(max_length=56)
    office = models.CharField(max_length=56)
    industry = models.CharField(max_length=56)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("engagement_app:engagement_landing",kwargs={'pk':self.pk})


class LocationNames(models.Model):
    engagement=models.OneToOneField(Engagement,related_name='locationnames', on_delete=models.CASCADE,unique=True,primary_key=True)
    mainlocation_name=models.CharField(max_length=56,default="Main Location", null=True, blank=True)
    subonelocation_name=models.CharField(max_length=56,default="Sub One Location", null=True, blank=True)
    subtwolocation_name=models.CharField(max_length=56,default="Sub Two Location", null=True, blank=True)
    subthreelocation_name=models.CharField(max_length=56,default="Sub Three Location", null=True, blank=True)

    def __str__(self):
        return '%s (%s) (%s) (%s)' % (self.mainlocation_name, self.subonelocation_name,self.subtwolocation_name,self.subthreelocation_name)

    def get_absolute_url(self):
        return reverse("engagement_app:engagement_landing",kwargs={'pk':self.engagement.id})
