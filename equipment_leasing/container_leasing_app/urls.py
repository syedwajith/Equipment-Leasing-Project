"""equipment_leasing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from container_leasing_app import views

urlpatterns = [
    path('home/', views.ContainerHome),
    path('adminlog/', views.adminlogin),
    path('admin/', views.home_admin),
    path('lessorlog/', views.lessorlogin),
    path('lessor/', views.home_lessor),
    path('lesseelog/', views.lesseelogin),
    path('lessee/', views.home_lessee),
    path('adminhome/', views.adminhome),
    path('lessorreg/', views.lessor_register),
    path('lessorlogreg/', views.lessor_log_reg),
    path('lesseereg/', views.lessee_register),
    path('lesseelogreg/', views.lessee_log_reg),
    path('lessor_home/', views.lessor_home),
    path('lessee_home/', views.lessee_home),
]
