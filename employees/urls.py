from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/',views.Dashboard,name='employee-dashboard'),
	path('add/employee',views.AddEmployee,name='add-employee'),
	path('update/<str:id>',views.UpdateEmployee,name='employee-update'),
	path('add/role',views.AddRole,name='add-role'),
	path('add/department',views.AddDepartment,name='add-department'),
	path('list/',views.EmployeeList,name='employee-list'),
	path('delete/<str:id>/',views.EmployeeDelete,name='employee-delete'),


]