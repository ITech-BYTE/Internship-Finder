from django.db import models
from django.contrib.auth.models import User

class Intern(models.Model):
    user = models.OneToOneField(User)
    dob = models.DateField()
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.username

class Company(models.Model):
    company_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User)
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.user.username

class Skill(models.Model):
    skill_id = models.CharField(max_length=5, unique=True)
    skill_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.skill_name

class Job(models.Model):
    job_id = models.CharField(max_length=20, unique=True)
    company = models.ForeignKey(Company)
    job_name = models.CharField(max_length=30)
    job_description = models.CharField(max_length=300)
    posting_date = models.DateField()

    def __unicode__(self):
        return self.job_name

class JobSkill(models.Model):
    skill = models.ForeignKey(Skill)
    job = models.ForeignKey(Job)


class InternSkill(models.Model):
    skill = models.ForeignKey(Skill)
    intern = models.ForeignKey(Intern)