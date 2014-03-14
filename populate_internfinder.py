import os

def populate():
    dummy_intro = "I have recently graduated from University with a distinction and I would like pursue an internship in" \
                  " programming to complement my degree.  I do not have any current work experience in programming however" \
                  " I have demonstrated excellent skills in this field throughout my time at university by consistently achieving high marks."

    # CREATE INTERN USERS
    arshad_user = add_user(username='arshad2k8', fname='Arshad', lname='Ahmed', password='ars', email='ar@s.com')
    user_arshad_intern = add_intern(user=arshad_user, dat='1990-01-01', intro=dummy_intro,education="Msc Computer Science")

    naz_user = add_user(username='naz2k8', fname='Naznin', lname='Deswalla', password='naz', email='na@s.com')
    user_naz_intern = add_intern(user=naz_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Software Engineering")

    dani_user = add_user(username='dani2k8', fname='Dani', lname='Patrick', password='dan', email='da@v.com')
    user_dani_intern = add_intern(user=dani_user, dat='1990-01-01', intro=dummy_intro,education="Msc Web Design and Development")

    joe_user = add_user(username='joe', fname='Joe', lname='Smith', password='pw', email='test@v.com')
    user_joe_intern = add_intern(user=joe_user, dat='1990-01-01', intro=dummy_intro,education="Msc Computer Science")

    john_user = add_user(username='john', fname='John', lname='Taylor', password='pw', email='test@v.com')
    user_john_intern = add_intern(user=john_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Information Technology")

    johny_user = add_user(username='johny', fname='Johny', lname='Last', password='pw', email='test@v.com')
    user_johny_intern = add_intern(user=johny_user, dat='1990-01-01', intro=dummy_intro,education="Msc Software Development")

    tommy_user = add_user(username='tommi', fname='Tommy', lname='Walker', password='ars', email='ar@s.com')
    user_tommy_intern = add_intern(user=tommy_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Software Development")

    masood_user = add_user(username='masood', fname='Masood', lname='Needajob', password='naz', email='na@s.com')
    user_masood_intern = add_intern(user=masood_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Computing Sciance")

    clarence_user = add_user(username='clarence', fname='Clarence', lname='Beaks', password='dav', email='da@v.com')
    user_clarence_intern = add_intern(user=clarence_user, dat='1990-01-01', intro=dummy_intro,education="Msc Web Development")

    claire_user = add_user(username='claire', fname='Claire', lname='Frempong', password='pat', email='pa@v.com')
    user_claire_intern = add_intern(user=claire_user, dat='1990-01-01', intro=dummy_intro,education="Msc Information Technology")

    mcdonald_user = add_user(username='mcdonald', fname='David', lname='McDonald', password='dan', email='da@v.com')
    user_mcdonald_intern = add_intern(user=mcdonald_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Mathematics")

    smith_user = add_user(username='smith', fname='Patrick', lname='Dixon', password='pw', email='test@v.com')
    user_smith_intern = add_intern(user=smith_user, dat='1990-01-01', intro=dummy_intro,education="Msc Economics")

    sarah_user = add_user(username='sarah', fname='Sarah', lname='Samuels', password='pw', email='test@v.com')
    user_sarah_intern = add_intern(user=sarah_user, dat='1990-01-01', intro=dummy_intro,education="Msc Computing Science")

    malcolm_user = add_user(username='malcolm', fname='Malcolm', lname='Hubbert', password='pw', email='test@v.com')
    user_malcolm_intern = add_intern(user=malcolm_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Software Engineering")

    kim_user = add_user(username='kim', fname='Kim', lname='Smilie', password='pw', email='test@v.com')
    user_kim_intern = add_intern(user=kim_user, dat='1990-01-01', intro=dummy_intro,education="Bsc Computing Science")


    #----------------------------------------------------------------------------------------------------#
    # CREATE INDUSTRIAL USERS

    desc_default = " We are currently looking for high flying students and fresh " \
               "graduates to undertake some of the IT internships."

    david_user = add_user(username='david2k8', fname='David', lname='Steiner', password='dav', email='da@v.com')
    desc_sky = "Skyscorner is known for being first to market with innovative software systems and solutions such as " \
               "Skyscorner Access within the airline industry."+desc_default
    user_david_sky_recruit = add_recruiter(user=david_user, comname = 'SKYSCORNER', url = "http://www.skyscorner.com/uk/en/", description=desc_sky)

    patrick_user = add_user(username='patric2k8', fname='Patrick', lname='Frempong', password='pat', email='pa@v.com')
    desc_amazone = "Amazone is known for being first to market with innovative software systems and solutions such as " \
                   "Amazone Access within the online retail."+desc_default
    user_patrick_amazone_recruit = add_recruiter(user=patrick_user, comname = 'Amazone', url = "https://www.amazone_recruitzone.com/", description=desc_amazone)

    jane_user = add_user(username='jane', fname='Jane', lname='Moyes', password='pw', email='test@v.com')
    desc_bayside = "Bayside Technologies is known for being first to market with innovative software systems and solutions " \
                   "such as Bayside Access within the marketing industry."+desc_default
    user_jane_bayside_recruit = add_recruiter(user=jane_user, comname = 'Bayside', url = "https://www.bayside_dummy.com/", description=desc_bayside)

    josh_user = add_user(username='josh', fname='Josh', lname='Hall', password='pw', email='test@v.com')
    desc_silicon = "Silicon is known for being first to market with innovative software systems and solutions such as " \
                   "Silicon Access within the manufacturing industry."+desc_default
    user_josh_silicon_recruit = add_recruiter(user=josh_user, comname = 'SILICON', url = "https://www.siliconit.com/", description=desc_silicon)

    catherine_user = add_user(username='cath', fname='Catherine', lname='Jenkins', password='pw', email='test@v.com')
    desc_ifr = "IFR is known for being first to market with innovative software systems and solutions such as IFR Access " \
               "within the recruitment industry."+desc_default
    user_catherine_ifr_recruit = add_recruiter(user=catherine_user, comname = 'IFR', url = "https://www.ifr-computing.com/", description=desc_ifr)

    samantha_user = add_user(username='sammy', fname='Samantha', lname='Walsh', password='pw', email='test@v.com')
    desc_soft = "Techsoft is known for being first to market with innovative software systems and solutions such as " \
                "Techsoft Access within the Technology industry."+desc_default
    user_samantha_techsoft_recruit = add_recruiter(user=samantha_user, comname = 'Techsoft', url = "https://www.softie.com/", description=desc_soft)

    mohammad_user = add_user(username='mohi', fname='Mohammad', lname='Shaffiq', password='pw', email='test@v.com')
    desc_sibeqo = "Sibeqo is known for being first to market with innovative software systems and solutions such as " \
                  "Sibeqo Access within the IT industry."+desc_default
    user_mohammad_sibeqo_recruit = add_recruiter(user=mohammad_user, comname = 'SIBEQO', url = "https://www.microsoft.com/", description=desc_sibeqo)


    # CREATE JOB OFFERS
    job_description = "We are currently recruiting for a programmer. No commercial experience is required but the " \
                      "candidate must have studied an IT related course and have had an exposure to programming. " \
                      "As a programmer you will be responsible for the analysis, design and coding of applications."

    # SKYSCORNER
    job_sky_develop = add_job(recruiter=user_david_sky_recruit, jobname='Software Developer', jobdesc=job_description,
                                            salary=1100,deadline='2014-06-18')
    job_sky_webdev = add_job(recruiter=user_david_sky_recruit, jobname='Web Developer Ruby', jobdesc=job_description,
                                           salary=1200, deadline='2014-07-25')
    job_sky_admin = add_job(recruiter=user_david_sky_recruit, jobname='System Admin', jobdesc=job_description,
                                             salary=900, deadline='2014-06-03')
    job_sky_webdev2 = add_job(recruiter=user_david_sky_recruit, jobname='Web Developer Python', jobdesc=job_description,
                                             salary=1600, deadline='2014-06-03')

    # AMAZONE
    job_amazone_analyst = add_job(recruiter=user_patrick_amazone_recruit, jobname='Software Analyst',
                                                    salary=800, jobdesc=job_description, deadline='2014-05-21')
    job_amazone_develop = add_job(recruiter=user_patrick_amazone_recruit, jobname='Java Developer',
                                                    salary=700, jobdesc=job_description, deadline='2014-08-25')

    # BAYSIDE
    job_bayside_design = add_job(recruiter=user_jane_bayside_recruit, jobname='Web Designer', jobdesc=job_description,
                                            salary=600,deadline='2014-06-18')
    job_bayside_anal = add_job(recruiter=user_jane_bayside_recruit, jobname='Programmer Analyst', jobdesc=job_description,
                                           salary=1200, deadline='2014-07-25')
    job_bayside_admin = add_job(recruiter=user_jane_bayside_recruit, jobname='Sys Admin', jobdesc=job_description,
                                             salary=2000, deadline='2014-06-03')

    # SILICON
    job_silicon_c = add_job(recruiter=user_josh_silicon_recruit, jobname='C++ Programmer', jobdesc=job_description,
                                            salary=1200,deadline='2014-06-18')
    job_silicon_java = add_job(recruiter=user_josh_silicon_recruit, jobname='Web Programmer', jobdesc=job_description,
                                           salary=1350, deadline='2014-07-25')

    # IFR
    job_ifr_python = add_job(recruiter=user_catherine_ifr_recruit, jobname='Python Developer', jobdesc=job_description,
                                            salary=1750,deadline='2014-06-18')
    job_ifr_ruby = add_job(recruiter=user_catherine_ifr_recruit, jobname='Ruby Developer', jobdesc=job_description,
                                           salary=1200, deadline='2014-07-25')
    job_ifr_php = add_job(recruiter=user_catherine_ifr_recruit, jobname='Php Developer', jobdesc=job_description,
                                             salary=1450, deadline='2014-06-03')

    # TECHSOFT
    job_ts_design = add_job(recruiter=user_samantha_techsoft_recruit, jobname='Web Designer', jobdesc=job_description,
                                            salary=960,deadline='2014-06-18')
    job_ts_java = add_job(recruiter=user_samantha_techsoft_recruit, jobname='Java Developer', jobdesc=job_description,
                                           salary=990, deadline='2014-07-25')

    #----------------------------------------------------------------------------------------------------#

    # add skills and populate new skills
    java_skill = add_skills(name='Java')
    c_skill = add_skills(name='C')
    python_skill = add_skills(name='Python')
    AD_skill = add_skills(name='Active Directory')
    report_skill = add_skills(name='Report Writing')
    cp_skill = add_skills(name='C++')
    ruby_skill = add_skills(name='Ruby')
    perl_skill = add_skills(name='Perl')
    php_skill = add_skills(name='PHP')
    django_skill = add_skills(name='Django')
    unix_skill = add_skills(name='Unix')

    #----------------------------------------------------------------------------------------------------#

    # APPLICATIONS
    # Applications for Sky Develop
    add_job_application(applicant=user_arshad_intern, job=job_sky_develop)
    add_job_application(applicant=user_joe_intern, job=job_sky_develop)
    add_job_application(applicant=user_dani_intern, job=job_sky_develop)
    add_job_application(applicant=user_johny_intern, job=job_sky_develop)
    add_job_application(applicant=user_claire_intern, job=job_sky_develop)
    add_job_application(applicant=user_arshad_intern, job=job_sky_webdev)
    add_job_application(applicant=user_masood_intern, job=job_sky_webdev)
    add_job_application(applicant=user_kim_intern, job=job_sky_webdev)
    add_job_application(applicant=user_sarah_intern, job=job_sky_admin)
    add_job_application(applicant=user_dani_intern, job=job_sky_admin)
    add_job_application(applicant=user_smith_intern, job=job_sky_webdev2)
    add_job_application(applicant=user_mcdonald_intern, job=job_sky_webdev2)
    add_job_application(applicant=user_malcolm_intern, job=job_sky_webdev2)

    # Applications for Amazone
    add_job_application(applicant=user_naz_intern, job=job_amazone_analyst)
    add_job_application(applicant=user_dani_intern, job=job_amazone_analyst)
    add_job_application(applicant=user_claire_intern, job=job_amazone_analyst)
    add_job_application(applicant=user_smith_intern, job=job_amazone_develop)
    add_job_application(applicant=user_mcdonald_intern, job=job_amazone_develop)
    add_job_application(applicant=user_masood_intern, job=job_amazone_develop)
    add_job_application(applicant=user_johny_intern, job=job_amazone_develop)

    # Applications for Bayside
    add_job_application(applicant=user_john_intern, job=job_bayside_anal)
    add_job_application(applicant=user_claire_intern, job=job_bayside_anal)
    add_job_application(applicant=user_kim_intern, job=job_bayside_design)
    add_job_application(applicant=user_clarence_intern, job=job_bayside_design)
    add_job_application(applicant=user_sarah_intern, job=job_bayside_design)
    add_job_application(applicant=user_tommy_intern, job=job_bayside_admin)
    add_job_application(applicant=user_dani_intern, job=job_bayside_admin)
    add_job_application(applicant=user_sarah_intern, job=job_bayside_admin)


    # Applications for Silicon
    add_job_application(applicant=user_john_intern, job=job_silicon_c)
    add_job_application(applicant=user_johny_intern, job=job_silicon_c)
    add_job_application(applicant=user_malcolm_intern, job=job_silicon_c)
    add_job_application(applicant=user_joe_intern, job=job_silicon_c)
    add_job_application(applicant=user_joe_intern, job=job_silicon_java)
    add_job_application(applicant=user_masood_intern, job=job_silicon_java)

    # Applications for IFR
    add_job_application(applicant=user_naz_intern, job=job_ifr_php)
    add_job_application(applicant=user_arshad_intern, job=job_ifr_php)
    add_job_application(applicant=user_tommy_intern, job=job_ifr_php)
    add_job_application(applicant=user_tommy_intern, job=job_ifr_python)
    add_job_application(applicant=user_smith_intern, job=job_ifr_python)
    add_job_application(applicant=user_sarah_intern, job=job_ifr_python)
    add_job_application(applicant=user_kim_intern, job=job_ifr_ruby)

    # Applications for Techsoft
    add_job_application(applicant=user_kim_intern, job=job_ts_design)
    add_job_application(applicant=user_mcdonald_intern, job=job_ts_design)
    add_job_application(applicant=user_clarence_intern, job=job_ts_java)
    add_job_application(applicant=user_claire_intern, job=job_ts_java)
    add_job_application(applicant=user_joe_intern, job=job_ts_java)



    #----------------------------------------------------------------------------------------------------#

    #	Adding skill requirements to job offers
    add_job_skills(skill=java_skill, job = job_sky_develop)
    add_job_skills(skill=cp_skill, job = job_sky_develop)
    add_job_skills(skill=unix_skill, job = job_sky_develop)
    add_job_skills(skill=unix_skill, job = job_sky_admin)
    add_job_skills(skill=ruby_skill, job = job_sky_webdev)
    add_job_skills(skill=python_skill, job = job_sky_webdev2)
    add_job_skills(skill=django_skill, job = job_sky_webdev2)

    add_job_skills(skill=java_skill, job = job_amazone_analyst)
    add_job_skills(skill=php_skill, job = job_amazone_develop)
    add_job_skills(skill=django_skill, job = job_amazone_develop)
    add_job_skills(skill=report_skill, job = job_amazone_analyst)

    add_job_skills(skill=unix_skill, job = job_bayside_admin)
    add_job_skills(skill=perl_skill, job = job_bayside_admin)
    add_job_skills(skill=php_skill, job = job_bayside_design)
    add_job_skills(skill=c_skill, job = job_bayside_anal)
    add_job_skills(skill=cp_skill, job = job_bayside_anal)

    add_job_skills(skill=java_skill, job = job_silicon_java)
    add_job_skills(skill=perl_skill, job = job_silicon_java)
    add_job_skills(skill=c_skill, job = job_silicon_c)
    add_job_skills(skill=cp_skill, job = job_silicon_c)
    add_job_skills(skill=AD_skill, job = job_silicon_c)

    add_job_skills(skill=python_skill, job = job_ifr_python)
    add_job_skills(skill=report_skill, job = job_ifr_python)
    add_job_skills(skill=django_skill, job = job_ifr_python)
    add_job_skills(skill=php_skill, job = job_ifr_php)
    add_job_skills(skill=report_skill, job = job_ifr_php)
    add_job_skills(skill=ruby_skill, job = job_ifr_ruby)
    add_job_skills(skill=php_skill, job = job_ifr_ruby)
    add_job_skills(skill=report_skill, job = job_ifr_ruby)


    #----------------------------------------------------------------------------------------------------#

    #	Adding skills to interns
    add_int_skills(skill = java_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = AD_skill, Internuser = user_arshad_intern)
    add_int_skills(skill = perl_skill, Internuser = user_arshad_intern)

    add_int_skills(skill = java_skill, Internuser = user_dani_intern)

    add_int_skills(skill = python_skill, Internuser = user_sarah_intern)
    add_int_skills(skill = ruby_skill, Internuser = user_sarah_intern)

    add_int_skills(skill = AD_skill, Internuser = user_claire_intern)
    add_int_skills(skill = python_skill, Internuser = user_claire_intern)
    add_int_skills(skill = cp_skill, Internuser = user_claire_intern)

    add_int_skills(skill = c_skill, Internuser = user_kim_intern)
    add_int_skills(skill = cp_skill, Internuser = user_kim_intern)
    add_int_skills(skill = unix_skill, Internuser = user_kim_intern)

    add_int_skills(skill = report_skill, Internuser = user_masood_intern)

    add_int_skills(skill = cp_skill, Internuser = user_joe_intern)
    add_int_skills(skill = report_skill, Internuser = user_joe_intern)
    add_int_skills(skill = ruby_skill, Internuser = user_joe_intern)

    add_int_skills(skill = perl_skill, Internuser = user_john_intern)
    add_int_skills(skill = php_skill, Internuser = user_john_intern)

    add_int_skills(skill = java_skill, Internuser = user_tommy_intern)
    add_int_skills(skill = report_skill, Internuser = user_tommy_intern)
    add_int_skills(skill = php_skill, Internuser = user_tommy_intern)

    add_int_skills(skill = php_skill, Internuser = user_smith_intern)
    add_int_skills(skill = unix_skill, Internuser = user_smith_intern)

    add_int_skills(skill = perl_skill, Internuser = user_mcdonald_intern)
    add_int_skills(skill = cp_skill, Internuser = user_mcdonald_intern)
    add_int_skills(skill = unix_skill, Internuser = user_mcdonald_intern)

    add_int_skills(skill = django_skill, Internuser = user_malcolm_intern)
    add_int_skills(skill = python_skill, Internuser = user_malcolm_intern)


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

def add_intern(user, dat, intro, education):
    p = Intern.objects.get_or_create(user=user, dob=dat, is_industrial=False, introduction=intro, education=education)[0]
    return p

def add_recruiter(user, comname, url, description):
    c = Recruiter.objects.get_or_create(user=user, company_name=comname, url=url, is_industrial=True, company_description=description)[0]
    return c

# add_skills is for Skill model class with skill_id and skill_name attributes and  skill_id is primary key
def add_skills(name):		#check the unique skill id
    c = Skill.objects.get_or_create(skill_name=name)[0]
    return c

# add_job method is for Job model class with job_id,company object as foreign key to Recruiter
#job_name job_description and posting_date attributes 		
#check job id required or not
def add_job(recruiter, jobname, jobdesc, deadline, salary):
    p = Job.objects.get_or_create(company=recruiter, job_name=jobname, job_description=jobdesc, deadline=deadline, salary=salary, location="Glasgow")[0]
    return p


def add_job_skills(skill, job):
    job.skills.add(skill)

def add_int_skills(skill, Internuser):
    Internuser.skills.add(skill)

def add_job_application(applicant, job):
    Application.objects.get_or_create(job=job, intern=applicant)





# Start execution here!
if __name__ == '__main__':
    print "Starting Intern Finder population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifinder.settings')
    from ifinder_main.models import Intern, Recruiter, Skill, Job, Application
    from django.contrib.auth.models import User
    populate()