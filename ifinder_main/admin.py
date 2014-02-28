__author__ = 'byte'


from django.contrib import admin
from ifinder_main.models import User, Intern, Recruiter, Job, Skill

admin.site.register(Intern)
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(Skill)