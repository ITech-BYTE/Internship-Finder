# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Count
from ifinder_main.forms import UserForm, InternForm, CompanyForm, UserEditForm
from ifinder_main.models import Job, Recruiter, Intern
from ifinder_main.utilities import get_job_list, get_user_type


# HOMEPAGE
# Shows a list of the most popular and latest offers
def home(request):
    context = RequestContext(request)

    context_dict = {}

    # These are the top 5 offers based on the number of applicants
    top_offers = Job.objects.annotate(applicant_count=Count('applicants')).order_by('-applicant_count')[:5]

    # These are the latest offers in the Job table based on the posting date
    latest_offers = Job.objects.order_by('-posting_date')[:5]

    user_type = get_user_type(request.user)

    # Add top offers and latest offers to the context dictionary
    context_dict['top_offers'] = top_offers
    context_dict['latest_offers'] = latest_offers
    context_dict['user_type'] = user_type

    return render_to_response("home.html", context_dict, context)

def my_home(request):
    user_type = get_user_type(request.user)

    # if the user is unregistered redirect to general homepage
    if user_type == 0:
        return HttpResponseRedirect('/')

    # if the user is a company redirect to company area
    elif user_type == 1:
        return HttpResponseRedirect('/company/home/')

    # if the user is an intern redirect to intern area
    else:
        return HttpResponseRedirect('/intern/home/')


# LOGOUT
# Logs out the user then redirects to the homepage
def user_logout(request):
    logout(request)

    # go back to homepage
    return HttpResponseRedirect('/')


# GENERAL REGISTRATION METHOD (interns: user_type=0, companies: user_type=1)
def register(request, reg_type):
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    registered = False

    # The action that will be passed to the template and that will be called when the user submits the form
    if reg_type == 1:
            action = "/intern/register/"
    elif reg_type == 0:
            action = "/company/register/"

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # Get information from the form depending on the registration type
        if reg_type == 1:
            profile_form = InternForm(data=request.POST)
        elif reg_type == 0:
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

            # Set the user profile's is_industrial variable to that we can decide later whether this profile
            # belongs to an intern or a company
            if reg_type == 1:
                profile.is_industrial = False
            elif reg_type == 0:
                profile.is_industrial = True

            # Now we save the UserProfile model instance.
            profile.save()

            # If it is an intern registration, also save skills
            if reg_type == 1:
                profile_form.save_m2m()

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
        if reg_type == 1:
            profile_form = InternForm()
        elif reg_type == 0:
            profile_form = CompanyForm()

    # Render the template depending on the context.
    return render_to_response(
        'register.html',
            {'is_reg': True, 'reg_type': reg_type,'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'action' : action, 'user_type': 0},
            context)

# LOGIN
def user_login(request):
    context = RequestContext(request)


    if request.method == 'POST':
        # get the username and password from the POST request
        username = request.POST["username"]
        password = request.POST["password"]

        # Try to authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # If the authentication was successful, log the user in and return to the homepage
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect('/')

            # If the account is disabled, show error to user
            else:
                return HttpResponse("Your account is disabled.")

        else:
            # If the user could not be found:
            print "Invalid login details: {0}, {1}".format(username,password)
            return render_to_response('error.html', {'error' : 'Invalid login details supplied' }, context)

    else:
        return render_to_response('login.html', {'user_type': 0}, context)


# PROFILE PAGE
# This is the profile view for both user types, only the form on the page is different depending on the user
@login_required
def profile(request):
    context = RequestContext(request)

    # A boolean value for telling the template whether the changes were successful.
    valid_change = False

    action = "/profile/"


    try:
        # Try to find the profile in interns
        current_user_profile = Intern.objects.get(user=request.user)

    except Intern.DoesNotExist:
        # If the user profile can't be found in interns, try looking for it in recruiters
        try:
            current_user_profile = Recruiter.objects.get(user=request.user)

        # This should not happen as only logged in users can access this page
        # However, the admin user is not an intern or a company
        except Recruiter.DoesNotExist:
            return render_to_response('error.html', {'error': "User could not be found. "},context)



    # If it's a HTTP POST, we're interested in processing form data.
    # This is analogous to the registration process.. Could we use the same function somehow?
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)

        if current_user_profile.is_industrial:
            profile_form = CompanyForm(data=request.POST, instance=current_user_profile)
        else:
            profile_form = InternForm(data=request.POST, instance=current_user_profile)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.save()

            profile_form.save_m2m()

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
        if current_user_profile.is_industrial:
            profile_form = CompanyForm(instance=current_user_profile)
        else:
            profile_form = InternForm(instance=current_user_profile)

    # Render the template depending on the context.
    user_type = get_user_type(request.user)
    reg_type = user_type - 1
    return render_to_response(
        'register.html',
            {'is_reg': False, 'reg_type': reg_type,'user_form': user_form, 'profile_form': profile_form, 'registered': valid_change,
             'action' : action, 'user_type': user_type},
            context)


# SEARCH PAGE
# Contains the search box on the page, which calls the suggest_job method on change.
# Shows the result set of suggest_job in a list.
def search(request):
    context = RequestContext(request)

    user_type = get_user_type(request.user)

    return render_to_response('search.html', {'user_type' : user_type}, context)

# Retrieves the list of jobs that contain the string from the search box in their name
def suggest_job(request):
    context = RequestContext(request)
    contains = ''

    if request.method == 'GET':
        print request.GET['suggestion']
        contains = request.GET['suggestion']    # Get the string to search for

    # Get 10 jobs which contain the string
    job_list = get_job_list(10, contains)

    # Render the jobs in a list
    return render_to_response('joblist.html', {'job_list' : job_list}, context)

def about(request):
    context = RequestContext(request)

    user_type = get_user_type(request.user)

    return render_to_response('about.html', {'user_type': user_type}, context)