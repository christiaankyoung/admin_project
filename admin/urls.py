"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from engagement_app import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.IndexView.as_view(),name='index'),
    path('engagements/',include('engagement_app.urls',namespace='engagement_app')),
    path('location/',include('location_app.urls',namespace='location_app')),
    path('inventory/',include('inventory_app.urls',namespace='inventory_app')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path("thanks/", views.ThanksPage.as_view(), name="thanks"),
    path('controls/',include('controls_app.urls',namespace='control_app')),
    path('count/',include('count_app.urls',namespace='count_app')),
    path('it/',include('it_app.urls',namespace='it_app')),
]
