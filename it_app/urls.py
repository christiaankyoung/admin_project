from django.urls import path
from it_app import views

app_name = 'it_app'

urlpatterns = [
    path('<int:pk>/',views.ApplicationDetailView.as_view(),name='application_detail'),
    path('<int:pk>/create/',views.ApplicationCreateView.as_view(),name='application_create'),
    path('update/<int:pk>/',views.ApplicationUpdateView.as_view(),name='application_update'),
    path('delete/<int:pk>/',views.ApplicationDeleteView.as_view(),name='application_delete'),
]
