from django.urls import path
from it_app import views

app_name = 'it_app'

urlpatterns = [
    path('<int:pk>/',views.ApplicationDetailView.as_view(),name='application_detail'),
    path('<int:pk>/create/',views.ApplicationCreateView.as_view(),name='application_create'),
    path('<int:en_pk>/update/<int:pk>/',views.ApplicationUpdateView.as_view(),name='application_update'),
    path('delete/<int:pk>/',views.ApplicationDeleteView.as_view(),name='application_delete'),
#report urls
    path('report/<int:pk>/',views.ReportDetailView.as_view(),name='report_detail'),
    path('<int:pk>/reportcreate/',views.ReportCreateView.as_view(),name='report_create'),
    path('<int:en_pk>/reportupdate/<int:pk>/',views.ReportUpdateView.as_view(),name='report_update'),
    path('reportdelete/<int:pk>/',views.ReportDeleteView.as_view(),name='report_delete'),
#mainlocation application urls
    path('<int:pk>/createmainlocationapplication/',views.MainLocationApplicationCreateView.as_view(),name='mainlocationapplication_associate'),
    path('<int:pk>/deletemainlocationapplication/',views.MainLocationApplicationDeleteView.as_view(),name='mainlocationapplication_unassociate'),
]
