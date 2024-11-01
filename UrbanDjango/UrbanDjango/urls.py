

"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from task4.views import index
from task5.views import main

urlpatterns = [
    #path('admin/', admin.site.urls),
    #
    #path('', TemplateView.as_view(template_name='menu.html')),
    #path('books/', TemplateView.as_view(template_name='books.html')),
    ##path('games/', TemplateView.as_view(template_name='videogames.html')),
    #path('games/', index, name='games'),
    #path('ok/', TemplateView.as_view(template_name='of couse.html')),
    #path('opana/', TemplateView.as_view(template_name='opana.html')),
    #path('magas/', TemplateView.as_view(template_name='magazin.html'))
    path('', main, name='main'),
]
