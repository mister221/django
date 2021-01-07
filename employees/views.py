from django.shortcuts import render,redirect
from .forms import  *

from .models import *

# Create your views here.

def Dashboard(request):
		employees_list = Employee.objects.all().count()
		department_list = Department.objects.all().count()
		role_list = Role.objects.all().count()
		employees = Employee.objects.all()[0:10]
		context = {
			'employees_list':employees,
			'employees':employees_list,
			'department':department_list,
			'role':role_list,
		}
		return render(request, 'employees/index.html',context)

def AddEmployee(request):
	if request.method == 'GET':
		form = EmployeeForm()

	else:
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/employee/dashboard')
	return render(request,'employees/employeeForm.html',{'form':form})

def UpdateEmployee(request,id):
	if request.method == 'GET':
		employee = Employee.objects.get(employee_id=id)
		form = EmployeeForm(instance=employee)
	else:
		employee = Employee.objects.get(employee_id=id)

		form = EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/employee/dashboard')
	return render(request,'employees/employeeForm.html',{'form':form})

def AddRole(request):
	if request.method == 'GET':
		form = RoleForm()
	else:
		form = RoleForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/employee/dashboard')
	return render(request,'employees/addRole.html',{'form':form})

def AddDepartment(request):
	if request.method == 'GET':
		form = DepartmentForm()
	else:
		form = DepartmentForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/employee/dashboard')
	return render(request,'employees/addDepartment.html',{'form':form})
	

def EmployeeList(request):
	
	employees = Employee.objects.all()

	context = {
		'objects':employees
	}

	return render(request,'employees/employeeList.html',context)

def EmployeeDelete(request,id):
	employee = Employee.objects.get(employee_id=id)
	employee.delete()
	return redirect('/employee/list')
	
