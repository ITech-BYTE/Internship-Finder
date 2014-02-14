from django.conf.urls import patterns, url
from ifinder_main import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'))