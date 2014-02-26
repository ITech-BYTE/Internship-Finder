# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ifinder_main.forms import UserForm, InternForm, CompanyForm
from ifinder_main.models import Job, JobSkill, Recruiter, Intern, UserProfile


# HOMEPAGE
def home(request):
    context = RequestContext(request)

    return render_to_response("home.html", {}, context)


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

    try:
        internship = Job.objects.get(id=internship_id)

        company = internship.company

        required_skills = JobSkill.objects.filter(job = internship)

        is_intern = False
        try:
            if request.user.is_authenticated():
                is_intern = Intern.objects.get(user=request.user)

        except UserProfile.DoesNotExist:
            pass

        context_dict['is_intern'] = is_intern

        context_dict['internship'] = internship

        context_dict['company'] = company

        context_dict['skills'] = required_skills

    except Job.DoesNotExist:
        pass

    return render_to_response('offer.html', context_dict, context)

# PROFILE PAGE
@login_required
def profile(request):
    return  HttpResponse("Profile Page")
