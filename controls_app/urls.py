from django.urls import path, include
from controls_app import views

app_name = 'controls_app'

urlpatterns = [
    path('detail/<int:pk>/',views.ControlDetailView.as_view(),name='control_detail'),
    path('<int:pk>/create/',views.ControlCreateView.as_view(),name='control_create'),
    path('<int:en_pk>/update/<int:pk>/',views.ControlUpdateView.as_view(),name='control_update'),
    path('delete/<int:pk>/',views.ControlDeleteView.as_view(),name='control_delete'),

    #mainlocation control urls
    path('<int:pk>/createmainlocationcontrol/',views.MainLocationControlCreateView.as_view(),name='mainlocationcontrol_associate'),
    path('<int:pk>/deletemainlocationcontrol/',views.MainLocationControlDeleteView.as_view(),name='mainlocationcontrol_unassociate'),

    #subonelocation control urls
    path('<int:pk>/createsubonelocationcontrol/',views.SubOneLocationControlCreateView.as_view(),name='subonelocationcontrol_associate'),
    path('<int:pk>/deletesubonelocationcontrol/',views.SubOneLocationControlDeleteView.as_view(),name='subonelocationcontrol_unassociate'),

    #Inventory Class control urls
    path('<int:pk>/createinventoryclasscontrol/',views.InventoryClassControlCreateView.as_view(),name='inventoryclasscontrol_associate'),
    path('<int:pk>/deleteInventoryclasscontrol/',views.InventoryClassControlDeleteView.as_view(),name='inventoryclasscontrol_unassociate'),

]
