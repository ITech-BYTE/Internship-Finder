from django.conf.urls import patterns, include, url
from ifinder_main.views import user_login, user_logout, home, profile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^ifinder/', include('ifinder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', home, name='home'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^intern/', include('ifinder_main.urls_intern')),
    url(r'^company/', include('ifinder_main.urls_company')),
)
