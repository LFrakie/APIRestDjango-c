"""APIRestDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

from rest_framework import routers
from apirest import views
from clientes.views import ClienteListView

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('clientes', views.ClienteViewSet) #Para llamr a la  ruta y la vista 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('clientes',ClienteListView.as_view(template_name="clientes/index.html"),name='listar')
  #  path('api-auth/', include('rest_framework.urls'))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
