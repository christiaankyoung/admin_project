from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import *

# Create your models here.
#inventory classes and relted models ie raw materials, finished goods
class InventoryClass(models.Model):
    classification = models.CharField(max_length=56)
    engagement = models.ForeignKey(Engagement,related_name='inventoryclass', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('classification','engagement')

    def __str__(self):
        return self.classification

    def get_absolute_url(self):
        return reverse("inventory_app:inventoryclass_detail",kwargs={'pk':self.pk})


#inventory types and related models ie chemicals, roll stock, wood chips
class InventoryType(models.Model):
    name = models.CharField(max_length=56)
    classification = models.ForeignKey(InventoryClass,related_name='inventorytype', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=False, default='')
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('name','classification')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':self.pk})

class InventoryTypeMainLocation(models.Model):
    type = models.ForeignKey(InventoryType,related_name='inventorytypemainlocation', on_delete=models.CASCADE)
    mainlocation = models.ForeignKey(MainLocation,related_name='inventorytypemainlocation', on_delete=models.CASCADE)
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('type','mainlocation')

    def __str__(self):
        return '%s (%s)' % (self.type, self.mainlocation)


    def get_absolute_url(self):
        inventory_id=self.type.id
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':inventory_id})

class InventoryTypeSubOneLocation(models.Model):
    type = models.ForeignKey(InventoryType,related_name='inventorytypesubonelocation', on_delete=models.CASCADE)
    subonelocation = models.ForeignKey(SubOneLocation,related_name='inventorytypesubonelocation', on_delete=models.CASCADE)
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('type','subonelocation')

    def __str__(self):
        return '%s (%s)' % (self.type, self.subonelocation)


    def get_absolute_url(self):
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':self.type.id})

class InventoryTypeSubTwoLocation(models.Model):
    type = models.ForeignKey(InventoryType,related_name='inventorytypesubtwolocation', on_delete=models.CASCADE)
    subtwolocation = models.ForeignKey(SubTwoLocation,related_name='inventorytypesubtwolocation', on_delete=models.CASCADE)
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('type','subtwolocation')

    def __str__(self):
        return '%s (%s)' % (self.type, self.subtwolocation)

    def get_absolute_url(self):
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':self.inventorytype.id})

class InventoryTypeSubThreeLocation(models.Model):
    type = models.ForeignKey(InventoryType,related_name='inventorytypesubthreelocation', on_delete=models.CASCADE)
    subthreelocation = models.ForeignKey(SubThreeLocation,related_name='inventorytypesubthreelocation', on_delete=models.CASCADE)
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('type','subthreelocation')

    def __str__(self):
        return '%s (%s)' % (self.type, self.subthreelocation)


    def get_absolute_url(self):
        return reverse("inventory_app:inventorytype_detail",kwargs={'pk':self.inventorytype.id})

#inventory sub type and related models ie strach, bleached, douglas fir
class InventorySubType(models.Model):
    name = models.CharField(max_length=56)
    type = models.ForeignKey(InventoryType,related_name='inventorysubtype', on_delete=models.CASCADE)
    balance = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('name','type')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventory_app:inventorysubtype_detail",kwargs={'pk':self.pk})
