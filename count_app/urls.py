from django.urls import path, include
from count_app import views

app_name = 'count_app'

urlpatterns = [
    path('detail/<int:pk>/',views.CountDetailView.as_view(),name='count_detail'),
    path('create/',views.CountCreateView.as_view(),name='count_create'),
    path('update/<int:pk>/',views.CountUpdateView.as_view(),name='count_update'),
    path('delete/<int:pk>/',views.CountDeleteView.as_view(),name='count_delete'),
]
