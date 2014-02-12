__author__ = 'byte'


from django.contrib import admin
from ifinder_main.models import User, Intern, Company, Job, Skill, JobSkill, InternSkill

admin.site.register(User)
admin.site.register(Intern)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(JobSkill)
admin.site.register(InternSkill)