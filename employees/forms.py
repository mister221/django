from django import forms

from django.db import models
from django.forms import ModelForm

from .models import (Employee,Department,Role,Leave,Attendance )
from bootstrap_datepicker_plus import DatePickerInput
class DepartmentForm(ModelForm):
	dept_mgr = forms.ModelChoiceField(queryset=Employee.objects.all(),empty_label='Dept Manager')
	class Meta:
		model = Department
		fields = "__all__"
		widgets = {
			'dept_id':forms.TextInput(attrs={'placeholder':'DeptId','class':'username'}),
			'dept_name':forms.TextInput(attrs={'placeholder':'Dept Name','class':'username'}),
			'dept_mgr':forms.TextInput(attrs={'placeholder':'Dept Mgr',}),
		}


class RoleForm(ModelForm):
	department = forms.ModelChoiceField(queryset = Department.objects.all(),empty_label="Select Department")
	class Meta:
		model = Role 
		fields = '__all__'

class EmployeeForm(ModelForm):
	role = forms.ModelChoiceField(queryset=Role.objects.all(),empty_label='Select Role')
	
	class Meta:
		model = Employee
		fields = '__all__'
		widgets = {
			'name' : forms.TextInput(attrs={'placeholder':'Name'}),
			'employee_id' : forms.TextInput(attrs={'placeholder':'Employee Id'}),
			'email' : forms.TextInput(attrs={'placeholder':'Email'}),
			'phone' : forms.TextInput(attrs={'placeholder':'Phone'}),
			'sex' : forms.TextInput(attrs={'placeholder':'sex'}),
			# 'role' : forms.TextInput(attrs={'placeholder':'Role'}),
			'address' : forms.TextInput(attrs={'placeholder':'Address'})

		}

class DateInput(forms.DateInput):
    input_type = 'date'


class LeaveForm(ModelForm):


	class Meta:
		model = Leave 
		fields = '__all__'
		widgets = {
            'date': DateInput(),
        }


class AttendanceForm(ModelForm):
	class Meta:
		model = Attendance 
		fields = '__all__'