from django import forms
from django.forms import extras
from ifinder_main.models import Intern, Recruiter, Skill, Job
from django.contrib.auth.models import User
from datetime import date


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter your username", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(help_text="Please enter your password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(help_text="Please enter your first name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(help_text="Please enter your last name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(help_text="Please enter your email", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(help_text="Please enter your first name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(help_text="Please enter your last name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(help_text="Please enter your email", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class InternForm(forms.ModelForm):
    dob = forms.DateField(help_text="Please enter your date of birth", widget=forms.extras.widgets.SelectDateWidget(attrs={'class':'form-control'},years=range(1980, date.today().year - 18)))
    skills = forms.ModelMultipleChoiceField(help_text="Please select your skills", queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Intern
        fields = ('dob','skills')


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=200, help_text="Please enter the name of your company.", widget=forms.TextInput(attrs={'class':'form-control'}))
    url = forms.URLField(max_length=200, help_text="Please enter the url of your website.", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Recruiter
        fields = ('url','company_name')


class InternshipForm(forms.ModelForm):
    job_name = forms.CharField(max_length=200, help_text="Please enter the name of your internship.", widget=forms.TextInput(attrs={'class':'form-control', 'size': 68}))
    job_description = forms.CharField(help_text="Please enter the description.", widget=forms.Textarea(attrs={'class': 'form-control','cols' : '70'}))
    skills = forms.ModelMultipleChoiceField(help_text="Please select the skills desired for this position.", queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Job
        fields = ('job_name', 'job_description', 'skills')