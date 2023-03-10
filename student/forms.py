from dataclasses import fields
import email
from email.policy import default
from faulthandler import disable
from lib2to3.pgen2.token import NUMBER
from multiprocessing.sharedctypes import Value
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from student.models import student_custom

# Create your forms here.

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     firstname =forms.CharField(max_length=20)
#     lastname =forms.CharField(max_length=20)

#     class meta:
# 	    model = User
#     fields = ["username","firstname","lastname", "email", "password1", "password2"]

#     def save(self, commit=True):
# 	    user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
# 	    if commit:
# 		    user.save()
# 	    return user
management_choise=[
    ('Student','Student'),
    ('Faculty','Faculty')
]
study_mode_choise=[
    # ('Select','Select'), 
    ('Online','Online'),
    ('On-Campus','On-Campus')
]
Approve_choise=[
    ('Approve','Approve'),
    ('Disapprove','Disapprove')
]

class signupform(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstname =forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname =forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Role = forms.CharField(label='What is your role?', widget=forms.RadioSelect(choices=management_choise))
    class Meta:
        model =student_custom
        fields =['firstname','lastname','email','Role']
    # def __init__(self, *args, **kwargs):
    #     super(signupform, self).__init__(*args, **kwargs)   
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'

class loginform1(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget = forms.PasswordInput,error_messages ={'required':"Emnter your password"},label='Password')
    def __init__(self, *args, **kwargs):
        super(loginform1, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class appliction_form(forms.Form):
    application_id=forms.CharField(max_length=10, required=True,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    university_name=forms.CharField(max_length=50, required=True)
    program_name=forms.CharField(max_length=50, required=True)
    study_mode=forms.ChoiceField(label='study mode:', choices=study_mode_choise)
    customer=forms.CharField(max_length=50, required=True,label='Student name')
    email=forms.EmailField(max_length=10, required=True,widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super(appliction_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class approve_from(forms.Form):
    select=forms.CharField(widget=forms.RadioSelect(choices=Approve_choise))

class application_id_student(forms.Form):
    id=forms.DecimalField(required=True,label="Application id",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Application number'}))

class reset_password_form(forms.Form):
    email=forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(reset_password_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
