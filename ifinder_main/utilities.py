from ifinder_main.models import Job, UserProfile, Intern, Recruiter
from django.db.models import Count

def get_job_list(max_results=0, contains=''):
    job_list = []

    if contains:
        job_list = Job.objects.filter(job_name__contains=contains)
    else:
        job_list = Job.objects.all()


    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results]

    return job_list


def get_also_applied_for(job):
    job_list = Job.objects.filter(applicants__in=job.applicants.all()).exclude(id=job.id).annotate(applications_in_common=Count('applicants')).order_by('-applications_in_common').filter(applications_in_common__gte=1)[:5]

    return job_list


def get_recommended(intern):
    exclude_IDs = []
    for job in intern.applications.all():
        exclude_IDs.append(job.id)

    job_list = Job.objects.exclude(id__in=exclude_IDs).filter(skills__in=intern.skills.all()).annotate(skills_in_common=Count('skills')).order_by('-skills_in_common').filter(skills_in_common__gte=1)[:5]

    return job_list



# returns the type of the user:
# 0 = unauthenticated
# 1 = company
# 2 = intern
# 3 = other authenticated (admin)
def get_user_type(user):
    if user.is_authenticated():
        try:
            # If the user profile can be found and is not an industrial user, set is_intern to True
            if UserProfile.objects.get(user=user).is_industrial:
                user_type = 1
            else:
                user_type = 2

        except UserProfile.DoesNotExist:
            user_type = 3
    else:
        user_type = 0

    return user_type


def get_is_applicant_of(intern, recruiter):
    rec = Recruiter.objects.filter(id=recruiter.id).filter(offers__in=intern.applications.all())
    return rec
