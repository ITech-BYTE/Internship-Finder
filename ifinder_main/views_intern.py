from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ifinder_main.models import Job, Intern, UserProfile, Recruiter, Application
from ifinder_main.views import register
from ifinder_main.utilities import get_recommended, get_also_applied_for, get_user_type, get_is_applicant_of


# INTERN REGISTRATION
def register_intern(request):
    return register(request, 1)

# APPLICATIONS
@login_required
def my_applications(request):
    context = RequestContext(request)

    context_dict = {}

    is_company = UserProfile.objects.get(user=request.user).is_industrial

    job_list = []

    if is_company:
        message = "This site is only available to interns."

    else:
        message = "You have applied for the following jobs:"

        intern = Intern.objects.get(user=request.user)
        job_list = Application.objects.filter(intern=intern)
        #job_list = Intern.objects.get(user=request.user).applications.all()

    context_dict['is_company'] = is_company
    context_dict['job_list'] = job_list
    context_dict['message'] = message
    context_dict['user_type'] = get_user_type(request.user)

    return render_to_response("intern/intern_jobs.html", context_dict, context)

# RECOMMENDED INTERNSHIPS
# Based on the skill set of the intern and the skills required by the internship
@login_required
def my_recommended(request):
    context = RequestContext(request)

    context_dict = {}

    is_company = UserProfile.objects.get(user=request.user).is_industrial

    job_list = []

    if is_company:
        return render_to_response('error.html', {'error': "This site is only available to interns."}, context)

    else:
        job_list = get_recommended(intern=Intern.objects.get(user=request.user))

    context_dict['job_list'] = job_list
    context_dict['user_type'] = get_user_type(request.user)

    return render_to_response("intern/recommended.html", context_dict, context)

@login_required()
def intern_details(request, intern_id):
    context = RequestContext(request)
    try:
        intern = Intern.objects.get(id=intern_id)
    except:
        return render_to_response('error.html', {'error': "Intern not found"}, context)

    user_type = get_user_type(request.user)

    permitted = False
    if user_type == 1:
        company = Recruiter.objects.get(user=request.user)

        if get_is_applicant_of(intern=intern, recruiter=company):
            return render_to_response('intern/intern_details.html', {'intern': intern, 'user_type': 1 }, context)

    return render_to_response('error.html', {'error': "You are not authorised to view this page."}, context)


# INTERNSHIP DETAILS
def internship_details(request, internship_id):
    context = RequestContext(request)

    context_dict = {}

    # This variable is set to True when the user has just applied for the job in order
    # to show successful registration notification on top
    just_applied = False

    try:
        # Try to find the internship by its ID
        internship = Job.objects.get(id=internship_id)

        required_skills = internship.skills.all()



        # Assume the user is not an intern by default
        user_type = get_user_type(request.user)


        if request.method == 'POST':
            # If it's a POST request, add the application to the DB
            Application.objects.get_or_create(intern=Intern.objects.get(user=request.user), job=internship)
            just_applied = True
            has_applied = True      # Let the template know that the user has already applied for the internship
        else:
            has_applied = False     # Assume the user has not applied for this job
            if user_type == 2:
                intern = Intern.objects.get(user=request.user)
                # If the intern is among the applicants, set has_applied to True
                if internship.applicants.filter(id = intern.id):
                    has_applied = True

        # Has the user just applied?
        context_dict['just_applied'] = just_applied

        # List of jobs that share applicants with this job
        # Ordered by the number of applicants in common
        context_dict['recommendations'] = get_also_applied_for(job=internship)

        # What is the type of the user?
        context_dict['user_type'] = user_type

        # Has the user applied for this job? If yes, we must not show the application button
        context_dict['has_applied'] = has_applied

        # The internship object this view is about
        context_dict['internship'] = internship

        # The company who offers this internship
        context_dict['company'] = internship.company

        # List of skills required by this offer
        context_dict['skills'] = required_skills

    except Job.DoesNotExist:
        pass

    return render_to_response('intern/offer.html', context_dict, context)