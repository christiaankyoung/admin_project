from django.urls import path, include
from controls_app import views

app_name = 'controls_app'

urlpatterns = [
    path('detail/<int:pk>/',views.ControlDetailView.as_view(),name='control_detail'),
    path('<int:pk>/create/',views.ControlCreateView.as_view(),name='control_create'),
    path('update/<int:pk>/',views.ControlUpdateView.as_view(),name='control_update'),
    path('delete/<int:pk>/',views.ControlDeleteView.as_view(),name='control_delete'),
]
