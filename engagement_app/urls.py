from django.urls import path, include
from engagement_app import views

app_name = 'engagement_app'

urlpatterns = [
    path('',views.EngagementListView.as_view(),name='engagement_list'),
    path('detail/<int:pk>/',views.EngagementDetailView.as_view(),name='engagement_detail'),
    path('create/',views.EngagementCreateView.as_view(),name='engagement_create'),
    path('update/<int:pk>/',views.EngagementUpdateView.as_view(),name='engagement_update'),
    path('delete/<int:pk>/',views.EngagementDeleteView.as_view(),name='engagement_delete'),
    path('<int:pk>/',views.EngagementLandingView.as_view(),name='engagement_landing'),
    #Location app urls
    path('location/',include('location_app.urls',namespace='location_app')),
    path('mainlocation/<int:pk>/',views.EngagementMainLocationDetailView.as_view(),name='engagement_mainlocation_detail'),
    path('locationtype/<int:pk>/',views.EngagementTypeLocationDetailView.as_view(),name='engagement_typelocation_detail'),
    path('<int:pk>/location/',views.LocationLandingView.as_view(),name='location_landing'),
    path('<int:pk>/locationtree/create',views.LocationTreeCreateView.as_view(),name='locationtree_create'),
    path('locationtree/update/<int:pk>/',views.LocationTreeUpdateView.as_view(),name='locationtree_update'),
    #Inventory app URLs
    path('inventory/',include('inventory_app.urls',namespace='inventory_app')),
    path('inventoryclass/<int:pk>/',views.EngagementInventoryClassDetailView.as_view(),name='engagement_inventoryclass_detail'),
    path('<int:pk>/inventory/',views.InventoryLandingView.as_view(),name='inventory_landing'),
    #count app URLs
    path('count/',include('count_app.urls',namespace='count_app')),
    path('<int:pk>/count/',views.CountLandingView.as_view(),name='count_landing'),
    path('counts/<int:pk>/',views.EngagementCountDetailView.as_view(),name='engagement_count_detail'),
    #controls app URLS
    path('controls/',include('controls_app.urls',namespace='controls_app')),
    path('<int:pk>/control/',views.ControlLandingView.as_view(),name='control_landing'),
    path('controls/<int:pk>/',views.EngagementControlDetailView.as_view(),name='engagement_control_detail'),
    #it app URLS
    path('it/',include('it_app.urls',namespace='it_app')),
    path('<int:pk>/it/',views.ITLandingView.as_view(),name='application_landing'),
    path('application/<int:pk>/',views.EngagementApplicationDetailView.as_view(),name='engagement_application_detail'),
]
