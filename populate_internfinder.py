import os

def populate():
    #Assume there are two Recruiters patrick2k8 and david2k8, and two Interns naz2k8 and arshad2k8
    arshad_user = add_user(username='arshad2k8', fname='Arshad', lname='Ahmed', password='ars', email='ar@s.com')
    naz_user = add_user(username='naz2k8', fname='Naznin', lname='Deswalla', password='naz', email='na@s.com')
    david_user = add_user(username='david2k8', fname='David', lname='Steiner', password='dav', email='da@v.com')
    patrick_user = add_user(username='patric2k8', fname='Patrick', lname='Frempong', password='pat', email='pa@v.com')
    dani_user = add_user(username='dani2k8', fname='Dani', lname='Patrick', password='dan', email='da@v.com')

    #Create New Intern Users
    user_arshad_intern = add_intern(user=arshad_user, dat='1990-01-01')
    user_naz_intern = add_intern(user=naz_user, dat='1990-01-01')

    #Create New Recruiter Users
    user_patrick_microsoft_recruit = add_recruiter(user=patrick_user, comname = 'MICROSOFT', url = "https://www.microsoft.com/")
    user_david_IBM_recruit = add_recruiter(user=david_user, comname = 'IBM', url = "http://www.ibm.com/uk/en/")

    #these methods create new Jobs and add those details
    job_david_IBM_recruit_develop = add_job(recruiter=user_david_IBM_recruit, jobname='Software Developer', jobdesc='programming', postingdate='2014-02-25')
    job_david_IBM_recruit_sysadmin = add_job(recruiter=user_patrick_microsoft_recruit, jobname='Software Analayst', jobdesc='Software Consultation', postingdate='2014-01-03')

    job_patrick_MICROSOFT_recruit_analyst = add_job(recruiter=user_david_IBM_recruit, jobname='System Admin', jobdesc='Administration', postingdate='2014-02-21')

    #all these methods add skills and populate new skills
    java_skill = add_skills(name='JAVA')
    c_skill = add_skills(name='C')
    python_skill = add_skills(name='PYTHON')
    AD_skill = add_skills(name='Active Directory')
    report_skill = add_skills(name='REPORT')


    #	Job Skils as foreign keys on Job and Skill objects
    add_job_skills(skill=java_skill, job = job_david_IBM_recruit_develop)
    add_job_skills(skill=AD_skill, job = job_david_IBM_recruit_sysadmin)
    add_job_skills(skill=python_skill, job = job_david_IBM_recruit_develop)

    #	Intern Skils as foreign keys on Skill and Intern objects
    add_int_skills(skill = java_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = python_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = report_skill, Internuser = user_arshad_intern)

    add_int_skills(skill = report_skill, Internuser = user_naz_intern)
    add_int_skills(skill = AD_skill, Internuser = user_naz_intern)
    add_int_skills(skill = c_skill, Internuser = user_naz_intern)


    # Print out what we have added to the user Intern. Prints all the skills of intern users
    for c in Intern.objects.all():
        for i in InternSkill.objects.filter(intern=c):
            print "- {0} - {1}".format(str(c), str(i))

    # Print out for all the Recruiter Users or company users all job they have posted
    for c in Recruiter.objects.all():
        for j in Job.objects.filter(company=c):
            print "- {0} - {1}".format(str(c), str(j))


def add_user(username, fname, lname, password, email):
    p = User.objects.get_or_create(username=username, first_name=fname, last_name=lname, email=email, password=password)[0]
    return p

def add_intern(user, dat):
    p = Intern.objects.get_or_create(user=user, dob=dat)[0]
    return p

def add_recruiter(user, comname, url):
    c = Recruiter.objects.get_or_create(user=user, company_name=comname, url=url)[0]
    return c
# add_skills is for Skill model class with skill_id and skill_name attributes and  skill_id is primary key	
def add_skills(name):		#check the unique skill id
    c = Skill.objects.get_or_create(skill_name=name)[0]
    return c

# add_job method is for Job model class with job_id,company object as foreign key to Recruiter
#job_name job_description and posting_date attributes 		
#check job id required or not
def add_job(recruiter, jobname, jobdesc, postingdate):
    p = Job.objects.get_or_create(company=recruiter, job_name=jobname, job_description=jobdesc, posting_date=postingdate)[0]
    return p


def add_job_skills(skill, job):
    p = JobSkill.objects.get_or_create(skill=skill, job=job)[0]
    return p

def add_int_skills(skill, Internuser):
    p = InternSkill.objects.get_or_create(skill=skill, intern=Internuser)[0]
    return p


# Start execution here!
if __name__ == '__main__':
    print "Starting Intern Finder population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifinder.settings')
    from ifinder_main.models import Intern, Recruiter, Skill, Job, JobSkill, InternSkill
    from django.contrib.auth.models import User
    populate()