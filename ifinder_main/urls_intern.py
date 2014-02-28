from django.conf.urls import patterns, url
from ifinder_main import views, views_intern

urlpatterns = patterns('',
        url(r'^register/$', views.register_intern, name='register'),
        url(r'^top/$', views_intern.top5, name='viewtop'),
        url(r'^offer/(?P<internship_id>\w+)/$', views.internship_details, name="internship_details")
)