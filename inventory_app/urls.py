from django.urls import path
from inventory_app import views

app_name = 'inventory_app'

urlpatterns = [
    #inventory class
    path('',views.InventoryClassListView.as_view(),name='inventoryclass_list'),
    path('<int:pk>/',views.InventoryClassDetailView.as_view(),name='inventoryclass_detail'),
    path('<int:pk>/createclass/',views.InventoryClassCreateView.as_view(),name='inventoryclass_create'),
    path('updateclass/<int:pk>/',views.InventoryClassUpdateView.as_view(),name='inventoryclass_update'),
    path('deleteclass/<int:pk>/',views.InventoryClassDeleteView.as_view(),name='inventoryclass_delete'),
    #inventory type
    path('type/<int:pk>/',views.InventoryTypeDetailView.as_view(),name='inventorytype_detail'),
    path('<int:pk>/createtype/',views.InventoryTypeCreateView.as_view(),name='inventorytype_create'),
    path('updatetype/<int:pk>/',views.InventoryTypeUpdateView.as_view(),name='inventorytype_update'),
    path('deletetype/<int:pk>/',views.InventoryTypeDeleteView.as_view(),name='inventorytype_delete'),

    #inventory location to type
    path('<int:pk>/createinventorymaintype/',views.InventoryTypeMainLocationCreateView.as_view(),name='inventory_maintype_associate'),
    path('<int:pk>/deleteinventorymaintype/',views.InventoryTypeMainLocationDeleteView.as_view(),name='inventory_maintype_unassociate'),
    path('<int:pk>/createinventorysubonetype/',views.InventoryTypeSubOneLocationCreateView.as_view(),name='inventory_subonetype_associate'),

    #Control inventory class urls
    path('<int:pk>/createcontrolinventoryclass/',views.ControlInventoryClassCreateView.as_view(),name='controlinventoryclass_associate'),

    #Control inventory types urls
    path('<int:pk>/createcontrolinventorytype/',views.ControlInventoryTypeCreateView.as_view(),name='controlinventorytype_associate'),
]
