from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path(r'^services/$', views.services, name='services'),
    re_path(r'^services/(?P<services_id>\d+)', views.services_detail, name='services_id'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^popreport/$', views.report, name='popreport'),
    re_path(r'^resources/$', views.resources, name='resources'),
    re_path(r'^smrpriceguide/$', views.smrpriceguide, name='smrpriceguide'),
    re_path(r'^store/$', views.store, name='store'),
    re_path(r'^events/$', views.events, name='events'),
]