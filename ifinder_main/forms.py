from django import forms
from ifinder_main import models
from ifinder_main.models import Intern
from ifinder_main.models import Recruiter
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class InternEditForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ('dob',)

class CompanyEditForm(forms.ModelForm):
    url = forms.URLField(max_length=200, help_text="Please enter the url of your website.")

    class Meta:
        model = Recruiter
        fields = ('url', 'company_name')

class InternForm(forms.ModelForm):

    class Meta:
        model = Intern
        fields = ('dob',)

class CompanyForm(forms.ModelForm):
    url = forms.URLField(max_length=200, help_text="Please enter the url of your website.")

    class Meta:
        model = Recruiter
        fields = ('url','company_name')