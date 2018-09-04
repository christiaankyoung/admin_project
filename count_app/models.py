from django.db import models
from django.urls import reverse
from engagement_app.models import Engagement
from location_app.models import MainLocation
from location_app.models import SubOneLocation
from inventory_app.models import InventoryType
from controls_app.models import Control
# Create your models here.
class InvCount(models.Model):
    ref = models.CharField(max_length=10)
    engagement = models.ForeignKey(Engagement,related_name='invcount', on_delete=models.CASCADE)
    inventorytype = models.ForeignKey(InventoryType,related_name='invcount', on_delete=models.CASCADE)
    mainlocation = models.ForeignKey(MainLocation,related_name='invcount', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    blindcount= models.BooleanField()
    control = models.ForeignKey(Control,related_name='invcount', on_delete=models.CASCADE, null=True, blank=True )



    class Meta:
        unique_together = ('ref','engagement')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("location_app:typelocation_detail",kwargs={'pk':self.pk})
