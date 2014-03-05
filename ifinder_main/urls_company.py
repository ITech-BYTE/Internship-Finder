from django.conf.urls import patterns, url
from ifinder_main.views_company import register_company

urlpatterns = patterns('',
        url(r'^register/$', register_company, name='register_company')    # Company registration page
)