from django.conf.urls import patterns, url
from ifinder_main import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^offer/(?P<internship_id>\w+)/$', views.internship_details, name="internship_details")
)