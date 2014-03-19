from ifinder_main.views import register
from django.template import RequestContext
from django.shortcuts import render_to_response
from ifinder_main.utilities import get_user_type
from ifinder_main.forms import InternshipForm
from ifinder_main.models import Job, Recruiter, Intern, UserProfile, Application, Skill
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


# COMPANY REGISTRATION
def register_company(request):
    return register(request, 0)

@login_required
def company_home(request):

    user_type = get_user_type(request.user)

    context = RequestContext(request)
    context_dict = {}
    context_dict['user_type'] = user_type


    if user_type == 1:
        company = Recruiter.objects.get(user=request.user)
        # lates three offers to show on the company welcome screen
        latest = company.offers.order_by('-posting_date')[:3]

        context_dict['latest'] = latest
        context_dict['company'] = company
        return render_to_response("company/company_home.html", context_dict, context)

    else:
        return render_to_response("error.html", {'error': "You have to be a company to view this page"}, context)

#Company User after logs in
@login_required
def my_offers(request):
    context = RequestContext(request)

    context_dict = {}

    user_type = get_user_type(request.user)

    # restrict page to recruiters
    if user_type != 1:
        return render_to_response('error.html', {'error' : "This section is only available to Company Users."}, context)


    else:
        # get the logged in user
        recruiter = Recruiter.objects.get(user=request.user)

        # get all the jobs for the recruiter
        job_list = recruiter.offers.all()
        context_dict['job_list'] = job_list
        context_dict['user_type'] = get_user_type(request.user)

        return render_to_response("company/company_jobs.html", context_dict, context)


@login_required
def get_applicants(request, internship_id):
    context = RequestContext(request)

    context_dict = {}

    is_company = (get_user_type(request.user) == 1)

    intern_list = []

    # restrict access to company users
    if is_company is False:
        message = "This section is only available to Company Users."

    else:
        message = "Interns List"
        job = Job.objects.get(id=internship_id)

        applications = Application.objects.filter(job=job)

    context_dict['is_company'] = is_company
    context_dict['applications'] = applications
    context_dict['message'] = message
    context_dict['user_type'] = get_user_type(request.user)

    return render_to_response("company/intern_applicants_list.html", context_dict, context)

@login_required
def add_job(request):
    return process_job(request, internship_id=0)

@login_required
def edit_job(request, internship_id):
    return process_job(request, internship_id=internship_id)

@login_required
def process_job(request, internship_id):
    context = RequestContext(request)

    user_type = get_user_type(request.user)

    # A boolean value for telling the template whether the internship was posted successfully.
    added = False

    # If the user is not a company user, show error
    if user_type != 1:
        render_to_response('error.html', {'error' : "This page is only available to company users."}, context)

    else:
        recruiter = Recruiter.objects.get(user=request.user)

        if internship_id != 0:
            internship = Job.objects.get(id=internship_id)

        # If it's a HTTP POST, we're interested in processing form data.
        if request.method == 'POST':
            # Attempt to grab information from the raw form information.
            if internship_id == 0:
                job_form = InternshipForm(data=request.POST)
            else:
                job_form = InternshipForm(data=request.POST, instance=internship)

            # If the form is valid...
            if job_form.is_valid():
                # Save the internship's form data to the database.
                internship = job_form.save(commit=False)

                # Set the company of the internship to the currently logged in recruiter
                internship.company = recruiter

                # Now we save the Job model instance.
                internship.save()

                # Save skills
                job_form.save_m2m()

                # Update our variable to tell the template registration was successful.
                added = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                print job_form.errors

        # Not a HTTP POST, so we render our form using a JobForm instance.
        # These forms will be blank, ready for user input.
        else:
            if internship_id == 0:
                job_form = InternshipForm()
            else:
                job_form = InternshipForm(instance=internship)


        # Render the template depending on the context.
        return render_to_response(
            'company/job_profile.html', {'id' : internship_id, 'job_form': job_form, 'added': added, 'user_type': 1}, context)

@login_required
def process_application(request, status):
    context = RequestContext(request)

    if request.method == 'GET':
        # process request if both IDs are available in the request
        if 'intern_id' in request.GET and 'job_id' in request.GET:
            try:
                recruiter = Recruiter.objects.get(user=request.user)

                intern = Intern.objects.get(id=request.GET['intern_id'])
                job = Job.objects.get(id=request.GET['job_id'])

                application = Application.objects.get(intern=intern,job=job)

                # restrict access to that user, who is offering the internship
                if job.company != recruiter:
                    return render_to_response('error.html', {'error': "You don't have the permission to accept interns for this job"}, context)

                application.status = status
                application.save()

                return render_to_response('company/process_application_feedback.html', {'status': status, 'intern': intern, 'user_type': 1}, context)

            # Invalid data
            except (Intern.DoesNotExist, Job.DoesNotExist, Application.DoesNotExist, Recruiter.DoesNotExist):
                return render_to_response('error.html', {'error': "Could not process your request"}, context)

        else:
            # Missing data
            return render_to_response('error.html', {'error': "Missing dictionary key"}, context)

    else:
        return render_to_response('error.html', {'error': "Something is wrong"}, context)


def accept_intern(request):
    return process_application(request=request, status="Accepted")


def decline_intern(request):
    return process_application(request=request, status="Declined")

def company_details(request, company_id):
    context = RequestContext(request)

    try:
        company = Recruiter.objects.get(id=company_id)

        user_type = get_user_type(request.user)

        return render_to_response('company/company_details.html', {'company': company, 'user_type': user_type}, context)

    except Recruiter.DoesNotExist:
        return render_to_response('error.html', {'error': "Company not found"}, context)

@login_required
def search_intern(request):
    context = RequestContext(request)

    user_type = get_user_type(request.user)

    # restrict access to recruiters
    if user_type != 1:
        return render_to_response('error.html', {'error': "This page is only available to companies"}, context)

    else:
        skills = Skill.objects.all()
        context_dict = {}
        context_dict['user_type'] = 1
        context_dict['skills'] = skills

        return render_to_response('company/search_intern.html', context_dict, context)


@login_required
def suggest_intern(request):
    context = RequestContext(request)

    contains = ''
    user_type = get_user_type(request.user)

    if request.method == 'GET' and user_type==1:
        skill = request.GET['skill_1']    # Get the string to search for
        skill_1 = Skill.objects.get(id=skill)

        company = Recruiter.objects.get(user=request.user)
        intern_IDs = Application.objects.filter(job=company.offers.all()).values_list('intern', flat=True)


        interns = Intern.objects.filter(skills=skill, id__in=intern_IDs)

        # Render the jobs in a list
        return render_to_response('company/internlist.html', {'intern_list' : interns}, context)

    else:
        return render_to_response('error.html', {'error': "Something went wrong"}, context)
