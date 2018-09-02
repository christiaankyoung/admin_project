from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
from inventory_app.models import InventoryClass


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
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False, default='')
    frequency_choices=((Yearly,'Yearly'),(Quarterly,'Quarterly'),(Monthly,'Monthly'),(Daily,'Daily'),(Occurance,'On Occurance'),(Other,'Other'))
    frequency = models.CharField(choices=frequency_choices,max_length=20, null=True)
    control_type_choices =((IT_APP,'IT APP Control'),(ITDM,'ITDM Control'),(Manual_Prevent,'Manual Prevent'),(Manual_Detect,'Manual Detect'))
    control_type = models.CharField(choices=control_type_choices,max_length=20,null=True)
    configurable = models.BooleanField( null=True)

    class Meta:
        unique_together = ('ref','engagement')
        ordering = ["ref"]

    def __str__(self):
        return self.ref

    def get_absolute_url(self):
        return reverse("control_app:control_detail",kwargs={'pk':self.pk})

    def get_control_type(self):
        result = {}
        for control in self:
            types=self.objects.all().order_by('control_type').distinct('control_type')
            if types not in result:
                result[types]=[]
            result[types].append(self.ref)
        return result

class MainLocationControl(models.Model):
    control = models.ForeignKey(Control,related_name='mainlocationcontrol', on_delete=models.CASCADE, blank=True)
    mainlocation = models.ForeignKey(MainLocation,related_name='mainlocationcontrol', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('control','mainlocation')

    def __str__(self):
        return '%s (%s)' % (self.mainlocation, self.control)

    def get_absolute_url(self):
        return reverse("location_app:mainlocation_detail",kwargs={'pk':self.mainlocation.id})

class SubOneLocationControl(models.Model):
    control = models.ForeignKey(Control,related_name='subonelocationcontrol', on_delete=models.CASCADE, blank=True)
    subonelocation = models.ForeignKey(SubOneLocation,related_name='subonelocationcontrol', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('control','subonelocation')

    def __str__(self):
        return '%s (%s)' % (self.subonelocation, self.control)

    def get_absolute_url(self):
        return reverse("location_app:subonelocation_detail",kwargs={'pk':self.subonelocation.id})

class InventoryClassControl(models.Model):
    control = models.ForeignKey(Control,related_name='inventoryclasscontrol', on_delete=models.CASCADE, blank=True)
    inventoryclass = models.ForeignKey(InventoryClass,related_name='inventoryclasscontrol', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('control','inventoryclass')

    def __str__(self):
        return '%s (%s)' % (self.inventoryclass, self.control)

    def get_absolute_url(self):
        return reverse("inventory_app:inventoryclass_detail",kwargs={'pk':self.inventoryclass.id})

class InventoryTypeControl(models.Model):
    control = models.ForeignKey(Control,related_name='inventorytypecontrol', on_delete=models.CASCADE, blank=True)
    inventorytype = models.ForeignKey(InventoryType,related_name='inventorytypecontrol', on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('control','inventorytype')

    def __str__(self):
        return '%s (%s)' % (self.inventorytype, self.control)

    def get_absolute_url(self):
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':self.inventorytype.id})
