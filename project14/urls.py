"""
URL configuration for project14 project.

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
from django.urls import path,include
from generic.views import *
from specific.views import *
import generic,specific

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generic1/',generic1,name='generic1'),
    path('specific1/',specific1,name='specific1'),
    path('generic/',include('generic.urls')),
    path('specific/',include('specific.urls')),
]
