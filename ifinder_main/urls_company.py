from django.conf.urls import patterns, url
from ifinder_main.views_company import register_company, my_offers, get_applicants, company_home, add_job, edit_job

urlpatterns = patterns('',
        url(r'^$', company_home, name='home'),    # Company registration page
        url(r'^register/$', register_company, name='register_company'),    # Company registration page
        url(r'^home/$', company_home, name='home_company'),    # Company registration page
        url(r'^applicants/$', my_offers, name='my_applications'), # List of applications of the logged in company
        url(r'^new_offer/$', add_job, name='new_offer'), # Add a new internship
        url(r'^offer/(?P<internship_id>\w+)/$', edit_job, name='new_offer'), # Add a new internship
        url(r'^applicants/(?P<internship_id>\w+)/$', get_applicants, name="Applicants_details"),   # Details of an internship by ID

)