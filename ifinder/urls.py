from django.conf.urls import patterns, include, url
from ifinder_main.views import user_login, user_logout, home, profile, search, suggest_job, about


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home, name='home'),                              # Homepage
                       url(r'^byte/$', about, name='about'),
                       url(r'^login/$', user_login, name='login'),                 # Login page
                       url(r'^logout/$', user_logout, name='logout'),              # Url to call logout function (redirected to homepage after logout)
                       url(r'^profile/$', profile, name='profile'),                # Profile page (for both interns and companies, depending in logged in user)
                       url(r'^search/$', search, name='search'),                   # Search page
                       url(r'^suggest_job/$', suggest_job, name='suggest'),        # Search result set embedded in search page
                       url(r'^admin/', include(admin.site.urls)),                  # Admin page
                       url(r'^intern/', include('ifinder_main.urls_intern')),      # Urls that start with /intern/
                       url(r'^company/', include('ifinder_main.urls_company')),    # Urls that start with /company/
)