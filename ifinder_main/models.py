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
    introduction = models.CharField(max_length=500)
    skills = models.ManyToManyField(Skill)
    education = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.username


class Recruiter(UserProfile):
    company_name = models.CharField(max_length=20, unique=True)
    company_description = models.CharField(max_length=400)
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.user.username


class Job(models.Model):
    company = models.ForeignKey(Recruiter, related_name='offers')
    skills = models.ManyToManyField(Skill)
    applicants = models.ManyToManyField(Intern, related_name='applications', through='Application')
    job_name = models.CharField(max_length=30)
    job_description = models.CharField(max_length=300)
    posting_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __unicode__(self):
        return self.job_name


class Application(models.Model):
    job = models.ForeignKey(Job)
    intern = models.ForeignKey(Intern)
    status = models.CharField(max_length=30, default="Pending")
