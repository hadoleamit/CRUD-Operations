from django import forms
from .models import *
from django.forms import ModelForm



class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    fields = ('fullname','emp_code','mobile','position')
    label ={
        'fullname':'Full Name',
        'emp_code':'Employee Code',
        'mobile'  :'Mobile',
        'position':'Position',
    }