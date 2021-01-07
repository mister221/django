from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.Attendance)
admin.site.register(models.Leave)
admin.site.register(models.Role)

