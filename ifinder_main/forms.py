from django import forms
from ifinder_main import models
from ifinder_main.models import Intern
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class InternForm(forms.ModelForm):

    class Meta:
        model = Intern
        fields = ('dob',)