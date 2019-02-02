"""tcg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import users.views
import services.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', users.views.login, name='login'),
    path('signup', users.views.signup, name='signup'),
    path('services', services.views.services, name='services'),
    path('services/<int:service_id>', services.views.services_detail, name='services_id'),
    path('', services.views.home, name='home'),
    path('popreport', services.views.report, name='popreport'),
    path('resources', services.views.resources, name='resources'),
    path('smrpriceguide', services.views.smrpriceguide, name='smrpriceguide'),
    path('store', services.views.store, name='store'),
    path('events', services.views.events, name='events'),
    
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
