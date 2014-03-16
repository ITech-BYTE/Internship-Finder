from django.conf.urls import patterns, url
from ifinder_main.views_company import register_company, my_offers, get_applicants, company_home, add_job, edit_job,\
    accept_intern, decline_intern, company_details, search_intern, suggest_intern

urlpatterns = patterns('',
        url(r'^register/$', register_company, name='register_company'),    # Company registration page
        url(r'^home/$', company_home, name='home_company'),    # Company home page
        url(r'^id/(?P<company_id>\w+)/$', company_details, name='company_details'),    # Company details page
        url(r'^my_offers/$', my_offers, name='my_applications'), # List of applications of the logged in company
        url(r'^new_offer/$', add_job, name='new_offer'), # Add a new internship
        url(r'^offer/(?P<internship_id>\w+)/$', edit_job, name='new_offer'), # Add a new internship
        url(r'^applicants/(?P<internship_id>\w+)/$', get_applicants, name="Applicants_details"),   # Details of an internship by ID
        url(r'^search/$', search_intern, name='search_intern'), # Browse interns
        url(r'^suggest_intern/$', suggest_intern, name='suggest_intern'), # Browse intern result area
        url(r'^accept/$', accept_intern, name='accept'),    # Accept an application
        url(r'^decline/$', decline_intern, name='decline'), # Decline an application
)