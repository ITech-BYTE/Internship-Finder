import os

def populate():
    # CREATE USERS
    arshad_user = add_user(username='arshad2k8', fname='Arshad', lname='Ahmed', password='ars', email='ar@s.com')
    naz_user = add_user(username='naz2k8', fname='Naznin', lname='Deswalla', password='naz', email='na@s.com')
    david_user = add_user(username='david2k8', fname='David', lname='Steiner', password='dav', email='da@v.com')
    patrick_user = add_user(username='patric2k8', fname='Patrick', lname='Frempong', password='pat', email='pa@v.com')
    dani_user = add_user(username='dani2k8', fname='Dani', lname='Patrick', password='dan', email='da@v.com')
    joe_user = add_user(username='joe', fname='Joe', lname='Smith', password='pw', email='test@v.com')
    john_user = add_user(username='john', fname='John', lname='Taylor', password='pw', email='test@v.com')
    johny_user = add_user(username='johny', fname='Johny', lname='Last', password='pw', email='test@v.com')

    #----------------------------------------------------------------------------------------------------#

    # CREATE INTERN USERS
    user_arshad_intern = add_intern(user=arshad_user, dat='1990-01-01')
    user_naz_intern = add_intern(user=naz_user, dat='1990-01-01')
    user_dani_intern = add_intern(user=dani_user, dat='1990-01-01')
    user_joe_intern = add_intern(user=joe_user, dat='1990-01-01')
    user_john_intern = add_intern(user=john_user, dat='1990-01-01')
    user_johny_intern = add_intern(user=johny_user, dat='1990-01-01')

    # CREATE INDUSTRIAL USERS
    user_patrick_microsoft_recruit = add_recruiter(user=patrick_user, comname = 'MICROSOFT', url = "https://www.microsoft.com/")
    user_david_IBM_recruit = add_recruiter(user=david_user, comname = 'IBM', url = "http://www.ibm.com/uk/en/")

    #----------------------------------------------------------------------------------------------------#

    # CREATE JOB OFFERS
    job_david_IBM_recruit_develop = add_job(recruiter=user_david_IBM_recruit, jobname='Software Developer', jobdesc='programming', postingdate='2014-01-18')
    job_david_IBM_recruit_webdev = add_job(recruiter=user_david_IBM_recruit, jobname='Web Developer', jobdesc='developing the IBM website', postingdate='2014-01-25')
    job_david_IBM_recruit_sysadmin = add_job(recruiter=user_david_IBM_recruit, jobname='System Admin', jobdesc='Administration', postingdate='2014-01-03')

    job_patrick_MICROSOFT_recruit_analyst = add_job(recruiter=user_patrick_microsoft_recruit, jobname='Software Analyst', jobdesc='Software Consultation', postingdate='2014-02-21')
    job_patrick_MICROSOFT_recruit_develop = add_job(recruiter=user_patrick_microsoft_recruit, jobname='Java Developer', jobdesc='programming', postingdate='2014-02-25')

    #----------------------------------------------------------------------------------------------------#

    # add skills and populate new skills
    java_skill = add_skills(name='JAVA')
    c_skill = add_skills(name='C')
    python_skill = add_skills(name='PYTHON')
    AD_skill = add_skills(name='Active Directory')
    report_skill = add_skills(name='REPORT')

    #----------------------------------------------------------------------------------------------------#

    # APPLICATIONS
    # Applications for IBM developer
    add_job_application(applicant=user_arshad_intern, job=job_david_IBM_recruit_develop)
    add_job_application(applicant=user_joe_intern, job=job_david_IBM_recruit_develop)
    add_job_application(applicant=user_john_intern, job=job_david_IBM_recruit_develop)
    add_job_application(applicant=user_naz_intern, job=job_david_IBM_recruit_develop)
    add_job_application(applicant=user_johny_intern, job=job_david_IBM_recruit_develop)

    # Applications for Microsoft analyst
    add_job_application(applicant=user_john_intern, job=job_patrick_MICROSOFT_recruit_analyst)
    add_job_application(applicant=user_dani_intern, job=job_patrick_MICROSOFT_recruit_analyst)
    add_job_application(applicant=user_arshad_intern, job=job_patrick_MICROSOFT_recruit_analyst)
    add_job_application(applicant=user_johny_intern, job=job_patrick_MICROSOFT_recruit_analyst)

    # Applications for IBM sysadmin
    add_job_application(applicant=user_naz_intern, job=job_david_IBM_recruit_sysadmin)
    add_job_application(applicant=user_dani_intern, job=job_david_IBM_recruit_sysadmin)
    add_job_application(applicant=user_joe_intern, job=job_david_IBM_recruit_sysadmin)

    # Applications for IBM web developer
    add_job_application(applicant=user_johny_intern, job=job_david_IBM_recruit_webdev)
    add_job_application(applicant=user_joe_intern, job=job_david_IBM_recruit_webdev)

    # Applications for Microsoft developer
    add_job_application(applicant=user_naz_intern, job=job_patrick_MICROSOFT_recruit_develop)

    #----------------------------------------------------------------------------------------------------#

    #	Adding skill requirements to job offers
    add_job_skills(skill=java_skill, job = job_david_IBM_recruit_develop)
    add_job_skills(skill=AD_skill, job = job_david_IBM_recruit_sysadmin)
    add_job_skills(skill=python_skill, job = job_david_IBM_recruit_develop)

    #----------------------------------------------------------------------------------------------------#

    #	Adding skills to interns
    add_int_skills(skill = java_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = python_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = report_skill, Internuser = user_arshad_intern)

    add_int_skills(skill = report_skill, Internuser = user_naz_intern)
    add_int_skills(skill = AD_skill, Internuser = user_naz_intern)
    add_int_skills(skill = c_skill, Internuser = user_naz_intern)

    #----------------------------------------------------------------------------------------------------#

    # Print out what we have added to the user Intern. Prints all the skills of intern users
    print "Intern skills added:"
    for c in Intern.objects.all():
        for i in c.skills.all():
            print "- {0} - {1}".format(str(c), str(i))

    # Print out for all the Recruiter Users or company users all job they have posted
    print "Companies and their offers:"
    for c in Recruiter.objects.all():
        for j in Job.objects.filter(company=c):
            print "- {0} - {1}".format(str(c), str(j))


    #----------------------------------------------------------------------------------------------------#
    # POPULATION HELPER METHODS

def add_user(username, fname, lname, password, email):
    p = User.objects.get_or_create(username=username, first_name=fname, last_name=lname, email=email)[0]
    p.set_password(password)
    return p

def add_intern(user, dat):
    p = Intern.objects.get_or_create(user=user, dob=dat, is_industrial=False)[0]
    return p

def add_recruiter(user, comname, url):
    c = Recruiter.objects.get_or_create(user=user, company_name=comname, url=url, is_industrial=True)[0]
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
    job.skills.add(skill)

def add_int_skills(skill, Internuser):
    Internuser.skills.add(skill)

def add_job_application(applicant, job):
    Application.objects.get_or_create(job=job, intern=applicant,accepted=False)





# Start execution here!
if __name__ == '__main__':
    print "Starting Intern Finder population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifinder.settings')
    from ifinder_main.models import Intern, Recruiter, Skill, Job, Application
    from django.contrib.auth.models import User
    populate()