from django.contrib import admin
from inventory_app.models import *
# Register your models here.

admin.site.register(InventoryClass)

admin.site.register(InventoryType)
admin.site.register(InventoryTypeMainLocation)
admin.site.register(InventoryTypeSubOneLocation)
admin.site.register(InventoryTypeSubTwoLocation)
admin.site.register(InventoryTypeSubThreeLocation)

admin.site.register(InventorySubType)
#admin.site.register(InventorySubTypeMainLocation)
#admin.site.register(InventorySubTypeSubOneLocation)
#admin.site.register(InventorySubTypeSubTwoLocation)
#admin.site.register(InventorySubTypeSubThreeLocation)
