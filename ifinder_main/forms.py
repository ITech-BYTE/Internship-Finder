from django import forms
from django.forms import extras
from ifinder_main.models import Intern, Recruiter, Skill, Job
from django.contrib.auth.models import User
from datetime import date


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, min_length=6, help_text="Please enter your username", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20, min_length=8,help_text="Please enter your password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, help_text="Please enter your first name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, help_text="Please enter your last name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(help_text="Please enter your email", widget=forms.TextInput(attrs={'class':'form-control'}))



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text="Please enter your first name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, help_text="Please enter your last name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(help_text="Please enter your email", widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if self.is_not_valid_email(data):
            raise forms.ValidationError("re-enter email")

        # Always return the cleaned data,
        # whether you have changed it or
        # not.
        return data

    def is_not_valid_email(email):

        if email.match(email):
                return False

        else: return True

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class InternForm(forms.ModelForm):
    dob = forms.DateField(help_text="Please enter your date of birth", widget=forms.extras.widgets.SelectDateWidget(attrs={'class':'form-control'},years=range(1980, date.today().year - 18)))
    skills = forms.ModelMultipleChoiceField(help_text="Please select your skills", queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())
    introduction = forms.CharField(max_length=2500, help_text="Please introduce yourself below.", widget=forms.Textarea(attrs={'class': 'form-control'}))
    education = forms.CharField(max_length=30, help_text="Please enter your most relevant education", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Intern
        fields = ('dob','skills', 'introduction', 'education')


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=200, help_text="Please enter the name of your company.", widget=forms.TextInput(attrs={'class':'form-control'}))
    company_description = forms.CharField(max_length=2000, help_text="Please enter the description of you company.", widget=forms.Textarea(attrs={'class': 'form-control'}))
    url = forms.URLField(max_length=200, help_text="Please enter the url of your website.", widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Recruiter
        fields = ('url', 'company_name', 'company_description')


class InternshipForm(forms.ModelForm):
    job_name = forms.CharField(max_length=50, help_text="Please enter the name of your internship.", widget=forms.TextInput(attrs={'class':'form-control'}))
    job_description = forms.CharField(max_length=2000,help_text="Please enter the description.", widget=forms.Textarea(attrs={'class': 'form-control'}))
    skills = forms.ModelMultipleChoiceField(help_text="Please select the skills desired for this position.", queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())
    deadline = forms.DateField(help_text="Please enter the deadline for application", widget=forms.extras.widgets.SelectDateWidget(attrs={'class':'form-control'}, years=range(date.today().year, date.today().year + 1)))
    salary = forms.IntegerField(help_text="Please enter the monthly salary.", min_value=500, max_value=3000, widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(max_length=200, help_text="Please enter the location of your internship.", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Job
        fields = ('job_name', 'job_description', 'skills', 'deadline', 'salary', 'location')