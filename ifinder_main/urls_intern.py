from django.conf.urls import patterns, url
from ifinder_main.views_intern import my_recommended, my_applications, internship_details, register_intern, intern_details

urlpatterns = patterns('',
        url(r'^register/$', register_intern, name='register'),                                    # Intern registration page
        url(r'^applications/$', my_applications, name='myapplications'),                          # List of applications of the logged in intern
        url(r'^recommend/$', my_recommended, name='myrecommended'),                               # Recommended jobs for the logged in intern
        url(r'^offer/(?P<internship_id>\w+)/$', internship_details, name="internship_details"),   # Details of an internship by ID
        url(r'^id/(?P<intern_id>\w+)/$', intern_details, name="intern_details")
)