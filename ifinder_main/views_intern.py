from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Count
from ifinder_main.forms import UserForm, InternForm, CompanyForm, InternEditForm, CompanyEditForm, UserEditForm
from ifinder_main.models import Job, Recruiter, Intern, UserProfile

def top5(request):
    context = RequestContext(request)

    context_dict = {}

    top_offers = Job.objects.annotate(applicant_count=Count('applicants')).order_by('-applicant_count')[:5]
    latest_offers = Job.objects.order_by('-posting_date')[:5]

    context_dict['top_offers'] = top_offers
    context_dict['latest_offers'] = latest_offers

    return render_to_response("topoffers.html", context_dict, context)