from django.db import models


from django.core.validators import RegexValidator
import datetime


#phone regex for employee class
phone_regex = RegexValidator(regex=r'^[6789]\d{9}$',message="invalid phone number")


#Create your models here.
class Department(models.Model):
    dept_id = models.CharField(max_length=10, primary_key=True)
    dept_name = models.CharField(max_length=20)
    dept_mgr = models.CharField(max_length=6)

    def __str__(self):
        return self.dept_name



class Role(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()

    sex_choice = (('M','Male'),('F','Female'),('Others','Others'),)

    sex = models.CharField(max_length=6,choices=sex_choice)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(validators=[phone_regex],max_length=10)
    address = models.TextField()
    # user_id = models.OneToOneField(User)


    def __str__(self):
        return self.employee_id




class Leave(models.Model):
    class meta:
        unique_together = (('employee_id','date'),)

    employee_id = models.ForeignKey(Employee,primary_key=True,on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    

    def __str__(self):
        
        return str(self.employee_id) +" On "+ str(self.date)


class Attendance(models.Model):
    
    employee_id = models.ForeignKey(Employee,primary_key=True,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    login_time = models.TimeField(auto_now_add=True)
    logout_time = models.TimeField(blank=True,null=True)
    class meta:
        unique_together = (('employee_id','date'),)

    def __str__(self):
        return self.employee_id  

    # def get_absolute_url(self):
    #     return redirect('employee/list')

    


