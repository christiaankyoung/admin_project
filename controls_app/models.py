from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
# Create your models here.
class Control(models.Model):
    engagement = models.ForeignKey(Engagement,related_name='control', on_delete=models.CASCADE)
    ref = models.CharField(max_length=10)
    frequency = models.CharField(choices=('Yearly','Quarterly','Monthly','Daily','On Occurance','Other'))
    control_type = models.CharField(choices=('IT APP Control','ITDM Control','Manual Prevent','Manual Detect'))




    class Meta:
        unique_together = ('ref','engagement')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("location_app:typelocation_detail",kwargs={'pk':self.pk})
