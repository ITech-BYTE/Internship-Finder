from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_industrial = models.BooleanField()

    def __unicode__(self):
        return self.user.username

class Skill(models.Model):
    skill_name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.skill_name


class Intern(UserProfile):
    dob = models.DateField()
    skills = models.ManyToManyField(Skill)

    def __unicode__(self):
        return self.user.username


class Recruiter(UserProfile):
    company_name = models.CharField(max_length=20, unique=True)
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.user.username


class Job(models.Model):
    company = models.ForeignKey(Recruiter, related_name='offers')
    skills = models.ManyToManyField(Skill)
    applicants = models.ManyToManyField(Intern, related_name='applications')
    job_name = models.CharField(max_length=30)
    job_description = models.CharField(max_length=300)
    posting_date = models.DateField(auto_now_add= True)

    def __unicode__(self):
        return self.job_name
