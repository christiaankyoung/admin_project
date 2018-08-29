from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
# Create your models here.
class Control(models.Model):
    ref = models.CharField(max_length=10)
    engagement = models.ForeignKey(Engagement,related_name='control', on_delete=models.CASCADE)
    inventorytype = models.ForeignKey(InventoryType,related_name='control', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    blindcount= models.BooleanField()



    class Meta:
        unique_together = ('ref','engagement')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("location_app:typelocation_detail",kwargs={'pk':self.pk})
