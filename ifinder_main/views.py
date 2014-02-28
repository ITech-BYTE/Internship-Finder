# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Count
from ifinder_main.forms import UserForm, InternForm, CompanyForm, InternEditForm, CompanyEditForm, UserEditForm
from ifinder_main.models import Job, Recruiter, Intern, UserProfile
from ifinder_main.jobsearch import get_job_list


# HOMEPAGE
def home(request):
    context = RequestContext(request)

    context_dict = {}

    top_offers = Job.objects.annotate(applicant_count=Count('applicants')).order_by('-applicant_count')[:5]
    latest_offers = Job.objects.order_by('-posting_date')[:5]

    context_dict['top_offers'] = top_offers
    context_dict['latest_offers'] = latest_offers

    return render_to_response("home.html", context_dict, context)

# LOGOUT
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')

# INTERN REGISTRATION
def register_intern(request):
    return register(request, 0)

# COMPANY REGISTRATION
def register_company(request):
    return register(request, 1)

# GENERAL REGISTRATION METHOD (interns: user_type=0, companies: user_type=1)
def register(request, user_type):
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    registered = False

    if user_type == 0:
            action = "/intern/register/"
    elif user_type == 1:
            action = "/company/register/"

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        if user_type == 0:
            profile_form = InternForm(data=request.POST)
        elif user_type == 1:
            profile_form = CompanyForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            if user_type == 0:
                profile.is_staff = True
            elif user_type == 1:
                profile.is_staff = False

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        if user_type == 0:
            profile_form = InternForm()
        elif user_type == 1:
            profile_form = CompanyForm()

    # Render the template depending on the context.
    return render_to_response(
        'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'action' : action},
            context)

# LOGIN
def user_login(request):
    context = RequestContext(request)


    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect('/')

            else:
                return HttpResponse("Your account is disabled.")

        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)

# INTERNSHIP DETAILS
def internship_details(request, internship_id):
    context = RequestContext(request)

    context_dict = {}

    just_applied = False

    try:
        internship = Job.objects.get(id=internship_id)

        company = internship.company

        required_skills = internship.skills.all()

        is_intern = False
        try:
            if request.user.is_authenticated():
                is_intern = not UserProfile.objects.get(user=request.user).is_industrial

        except UserProfile.DoesNotExist:
            pass

        if request.method == 'POST':
            internship.applicants.add(Intern.objects.get(user=request.user))
            just_applied = True
            has_applied = True
        else:
            has_applied = False
            if is_intern:
                intern = Intern.objects.get(user=request.user)
                if internship.applicants.filter(id = intern.id):
                    has_applied = True

        context_dict['just_applied'] = just_applied

        context_dict['is_intern'] = is_intern

        context_dict['has_applied'] = has_applied

        context_dict['internship'] = internship

        context_dict['company'] = company

        context_dict['skills'] = required_skills

    except Job.DoesNotExist:
        pass

    return render_to_response('offer.html', context_dict, context)

# PROFILE PAGE
@login_required
def profile(request):
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    valid_change = False


    try:
        current_userprofile = Intern.objects.get(user=request.user)

    except Intern.DoesNotExist:
        try:
            current_userprofile = Recruiter.objects.get(user=request.user)

        except Recruiter.DoesNotExist:
            return render_to_response('error.html', {'error': "User could not be found. "},context)



    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)

        if current_userprofile.is_industrial:
            profile_form = CompanyEditForm(data=request.POST, instance=current_userprofile)
        else:
            profile_form = InternEditForm(data=request.POST, instance=current_userprofile)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.save()

            # Update our variable to tell the template registration was successful.
            valid_change = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print profile_form.errors, user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserEditForm(instance=request.user)
        if current_userprofile.is_industrial:
            profile_form = CompanyEditForm(instance=current_userprofile)
        else:
            profile_form = InternEditForm(instance=current_userprofile)

    # Render the template depending on the context.
    return render_to_response(
        'profile.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': valid_change},
            context)


def search(request):
    context = RequestContext(request)

    return render_to_response('search.html', {}, context)


def suggest_job(request):
    context = RequestContext(request)
    job_list =[]
    contains = ''

    if request.method == 'GET':
        print request.GET['suggestion']
        contains = request.GET['suggestion']

    job_list = get_job_list(10, contains)

    return render_to_response('joblist.html', {'job_list' : job_list}, context)
