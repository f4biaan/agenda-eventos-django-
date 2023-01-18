"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from eventos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_eventos, name=''),
    path('create_evento/', views.create_evento, name='create_evento'),
    path('update_eventos/<int:id>/', views.update_eventos, name='update_eventos'),
    path('delete_eventos/<int:id>/', views.delete_eventos, name='delete_eventos'),
]
