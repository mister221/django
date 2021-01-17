from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
	class meta:
		model = 'User'
		fields = ['username','password1','password2']
		widgets = {
			'username' : forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),
		}