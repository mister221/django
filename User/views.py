from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def UserRegister(request):
	if request.method == 'GET':
		form = UserRegisterForm()
	else:
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/login')
	context = {
		'form':form
	}

	return render(request,'User/register.html',context)

def UserLogin(request):
	context = {}

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request,username=username,password=password)

		if user:
			login(request,user)
			return redirect('/employee/dashboard')
		else:
			context = {
				'error':'please provide correct user info'
			}
	return render(request,'User/login.html',context)

def UserLogout(request):
	logout(request)
	return redirect('/login')