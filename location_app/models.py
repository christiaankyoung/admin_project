from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
# Create your models here.
class TypeLocation(models.Model):
    type = models.CharField(max_length=256)
    engagement = models.ForeignKey(Engagement,related_name='typelocation', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('type','engagement')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("location_app:typelocation_detail",kwargs={'pk':self.pk})


class MainLocation(models.Model):
    name = models.CharField(max_length=256)
    engagement = models.ForeignKey(Engagement,related_name='mainlocation', on_delete=models.CASCADE)
    address = models.CharField(max_length=256,null=True, blank=False, default='')
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','engagement')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_app:mainlocation_detail",kwargs={'pk':self.pk})

    def get_inventory_types_by_class(self):
        result = {}
        for inventorytype in self.inventorytypemainlocation.all():
            cls=inventorytype.type.classification
            if cls not in result:
                result[cls]=[]
            result[cls].append(inventorytype)
        return result

    def get_aggregate_inventory_balance(self):
        subsone=self.subonelocation.all()
        substwo=[]
        result={}
        for inventorytype in self.inventorytypemainlocation.all():
            if inventorytype.type not in result:
                result[inventorytype.type]=0
            result[inventorytype.type] += inventorytype.balance

        for sub in subsone:
            substwo.extend(list(sub.subtwolocation.all()))
            for inventorytype in sub.inventorytypesubonelocation.all():
                if inventorytype.type not in result:
                    result[inventorytype.type]=0
                result[inventorytype.type] += inventorytype.balance
        for sub in substwo:
            for inventorytype in sub.inventorytypesubtwolocation.all():
                if inventorytype.type not in result:
                    result[inventorytype.type]=0
                result[inventorytype.type] += inventorytype.balance
        return result



class MainLocationInfo(models.Model):
    type = models.ForeignKey(TypeLocation,related_name='mainlocationinfotype', on_delete=models.CASCADE, blank=True)
    mainlocation = models.ForeignKey(MainLocation,related_name='mainlocationinfo', on_delete=models.CASCADE, blank=True, limit_choices_to={})
    balance =models.IntegerField(null=True)

    class Meta:
        unique_together = ('type','mainlocation')

    def __str__(self):
        return '%s (%s)' % (self.mainlocation, self.type)

    def get_absolute_url(self):
        return reverse("location_app:mainlocation_detail",kwargs={'pk':self.mainlocation.id})


#sub location 1 with info
class SubOneLocation(models.Model):
    name = models.CharField(max_length=256)
    mainlocation = models.ForeignKey(MainLocation,related_name='subonelocation', on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=True, blank=False, default='')
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','mainlocation')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_app:subonelocation_detail",kwargs={'pk':self.id,'ml_pk':self.mainlocation.id})

    def get_inventory_types_by_class(self):
        result = {}
        for inventorytype in self.inventorytypesubonelocation.all():
            cls=inventorytype.type.classification
            if cls not in result:
                result[cls]=[]
            result[cls].append(inventorytype)
        return result

class SubOneLocationInfo(models.Model):
    type = models.ForeignKey(TypeLocation,related_name='subonelocationinfotype', on_delete=models.CASCADE, blank=True)
    subonelocation = models.ForeignKey(SubOneLocation,related_name='subonelocationinfo', on_delete=models.CASCADE, blank=True)


    class Meta:
        unique_together = ('type','subonelocation')

    def __str__(self):
        return '%s (%s)' % (self.subonelocation, self.type)

    def get_absolute_url(self):
        return reverse("location_app:subonelocation_detail",kwargs={'pk':self.subonelocation.id,'ml_pk':self.subonelocation.mainlocation.id})

# sub location 2 with info
class SubTwoLocation(models.Model):
    name = models.CharField(max_length=256)
    subonelocation = models.ForeignKey(SubOneLocation,related_name='subtwolocation', on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=True, blank=False, default='')
    description = models.TextField(null=True, blank=False, default='')

    class Meta:
        unique_together = ('name','subonelocation')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_app:subtwolocation_detail",kwargs={'pk':self.pk})

class SubTwoLocationInfo(models.Model):
    type = models.ForeignKey(TypeLocation,related_name='subtwolocationinfotype', on_delete=models.CASCADE, blank=True)
    subtwolocation = models.ForeignKey(SubTwoLocation,related_name='subtwolocationinfo', on_delete=models.CASCADE, blank=True)


    class Meta:
        unique_together = ('type','subtwolocation')

    def __str__(self):
        return '%s (%s)' % (self.subtwolocation, self.type)

    def get_absolute_url(self):
        return reverse("location_app:subtwolocation_detail",kwargs={'pk':self.subtwolocation.id})

# sub location 3 with info
class SubThreeLocation(models.Model):
    name = models.CharField(max_length=256)
    subtwolocation = models.ForeignKey(SubTwoLocation,related_name='subthreelocation', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name','subtwolocation')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_app:subthreelocation_detail",kwargs={'pk':self.pk})

class SubThreeLocationInfo(models.Model):
    type = models.ForeignKey(TypeLocation,related_name='subthreelocationinfotype', on_delete=models.CASCADE, blank=True)
    subthreelocation = models.ForeignKey(SubThreeLocation,related_name='subthreelocationinfo', on_delete=models.CASCADE, blank=True)


    class Meta:
        unique_together = ('type','subthreelocation')

    def __str__(self):
        return '%s (%s)' % (self.subthreelocation, self.type)

    def get_absolute_url(self):
        return reverse("location_app:subthreelocation_detail",kwargs={'pk':self.subthreelocation.id})
