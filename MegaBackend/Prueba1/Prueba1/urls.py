"""
URL configuration for Prueba1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from megaaplicacion import views as app1



urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", app1.display1, name= "index"),
    path("Razas/", app1.display2, name= "raza"),
    path("quiltro/", app1.display3, name= "quiltro"),
    path("mescla/", app1.display4, name= "mescla"),
]
