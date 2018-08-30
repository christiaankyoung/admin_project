from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
# Create your models here.
class Control(models.Model):
    Yearly='Yearly'
    Quarterly='Quarterly'
    Monthly='Monthly'
    Daily='Daily'
    Occurance='On Occurance'
    Other='Other'
    IT_APP='IT APP Control'
    ITDM='ITDM Control'
    Manual_Prevent='Manual Prevent'
    Manual_Detect='Manual Detect'

    engagement = models.ForeignKey(Engagement,related_name='control', on_delete=models.CASCADE)
    ref = models.CharField(max_length=10)
    frequency_choices=((Yearly,'Yearly'),(Quarterly,'Quarterly'),(Monthly,'Monthly'),(Daily,'Daily'),(Occurance,'On Occurance'),(Other,'Other'))
    frequency = models.CharField(choices=frequency_choices,max_length=20, null=True)
    control_type_choices =((IT_APP,'IT APP Control'),(ITDM,'ITDM Control'),(Manual_Prevent,'Manual Prevent'),(Manual_Detect,'Manual Detect'))
    control_type = models.CharField(choices=control_type_choices,max_length=20,null=True)
    configurable = models.BooleanField(help_text="Is this control configurable?", null=True)

    class Meta:
        unique_together = ('ref','engagement')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("control_app:control_detail",kwargs={'pk':self.pk})
