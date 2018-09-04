from django.urls import path
from location_app import views

app_name = 'location_app'

urlpatterns = [
    path('',views.MainLocationListView.as_view(),name='mainlocation_list'),
    path('<int:pk>/',views.MainLocationDetailView.as_view(),name='mainlocation_detail'),
    path('<int:pk>/create/',views.MainLocationCreateView.as_view(),name='mainlocation_create'),
    path('update/<int:pk>/',views.MainLocationUpdateView.as_view(),name='mainlocation_update'),
    path('delete/<int:pk>/',views.MainLocationDeleteView.as_view(),name='mainlocation_delete'),
    #TypeLocation URLS
    path('<int:pk>/createtype/',views.TypeLocationCreateView.as_view(),name='typelocation_create'),
    path('updatetype/<int:pk>/',views.TypeLocationUpdateView.as_view(),name='typelocation_update'),
    path('type/<int:pk>/',views.TypeLocationDetailView.as_view(),name='typelocation_detail'),
    path('deletetype/<int:pk>/',views.TypeLocationDeleteView.as_view(),name='typelocation_delete'),
    path('',views.TypeLocationListView.as_view(),name='typelocation_list'),
    #Main Location info
    path('<int:pk>,main-type-associate/',views.MainTypeCreateView.as_view(),name='main-type_associate'),
    path('<int:pk>,main-type-associate/unassociate/',views.MainTypeDeleteView.as_view(),name='main-type_unassociate'),
    #engagemant main location views
    path('mainlocation/engagement/<int:pk>/',views.MainLocationEngagementDetailView.as_view(),name='engagement_location_detail'),
    #Sub One urls
    path('<int:pk>/createsubone/',views.SubOneLocationCreateView.as_view(),name='subonelocation_create'),
    path('<int:ml_pk>/<int:pk>/',views.SubOneLocationDetailView.as_view(),name='subonelocation_detail'),
    path('updatesubone/<int:pk>/',views.SubOneLocationUpdateView.as_view(),name='subonelocation_update'),
    path('deletesubone/<int:pk>/',views.SubOneLocationDeleteView.as_view(),name='subonelocation_delete'),
    #SubOne Location info
    path('<int:pk>,subone-type-associate/',views.SubOneTypeCreateView.as_view(),name='subone-type_associate'),
    path('<int:pk>,subone-type-associate/unassociate/',views.SubOneTypeDeleteView.as_view(),name='subone-type_unassociate'),
    #SubTwo
    path('<int:pk>/createsubtwo/',views.SubTwoLocationCreateView.as_view(),name='subtwolocation_create'),
    path('<int:ml_pk>/<int:so_pk>/<int:pk>',views.SubTwoLocationDetailView.as_view(),name='subtwolocation_detail'),
    path('updatesubtwo/<int:pk>/',views.SubTwoLocationUpdateView.as_view(),name='subtwolocation_update'),
    path('deletesubtwo/<int:pk>/',views.SubTwoLocationDeleteView.as_view(),name='subtwolocation_delete'),
    #Control mainlocaion urls
    path('<int:pk>/createcontrolmainlocation/',views.ControlMainLocationCreateView.as_view(),name='controlmainlocation_associate'),
    #Control mainlocaion urls
    path('<int:pk>/createcontrolsubonelocation/',views.ControlSubOneLocationCreateView.as_view(),name='controlsubonelocation_associate'),
]
