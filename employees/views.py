from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import  *

from .models import *
import datetime

# Create your views here.

def Dashboard(request):
		employees_list = Employee.objects.all().count()
		department_list = Department.objects.all().count()
		role_list = Role.objects.all().count()
		employees = Employee.objects.all()[0:10]
		attendance_count = Attendance.objects.filter(date=datetime.datetime.now().date()).count()
		context = {
			'employees_list':employees,
			'employees':employees_list,
			'department':department_list,
			'role':role_list,
			'attendance':attendance_count,
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

def EmployeeDetailView(request,id):
	employee = Employee.objects.get(employee_id=id)
	return render(request,'employees/employeeDetail.html',{'employee':employee})
	
def EmployeeAttendance(request,id=0):
	
	form = ''
	created = Attendance.objects.filter(employee_id=id,date=datetime.datetime.now().date())
	if not created:

		form = Attendance(id)

		form.date = datetime.datetime.now().date()
		form.login_time = datetime.datetime.now() 
		created = Attendance.objects.filter(employee_id =id)
		
		form.save()
	
	# return redirect('/employee/detail/'+id)
	else:
		form = 'already logged in'
	return redirect('/employee/detail/'+id)
	

def EmployeeAttendanceLogout(request,id):
	form = Attendance.objects.get(employee_id=id,date=datetime.datetime.now().date())
	form.logout_time = datetime.datetime.now()
	form.save()

	return redirect('/employee/detail/'+id)

def EmployeeLeave(request,id):
	if request.method == 'GET':
		data = {'employee_id':id}
		form = LeaveForm(initial=data)
		
	else:
		form = LeaveForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/employee/detail/'+id)
	context = {
		'form':form
	}

	return render(request,'employees/leaveform.html',context)