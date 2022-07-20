from django.contrib import admin
from . import models

# Register your models here.
class HrAdminArea(admin.AdminSite):
    site_header = 'HR Admin Area'
    index_title = 'HRMS'
    site_title = 'HRMS'

hr_site = HrAdminArea(name='HR_Admin')

# Admin Area
admin.site.register(models.Department)
admin.site.register(models.Job)
admin.site.register(models.Employee)
admin.site.register(models.EnrollImage)
admin.site.register(models.Attendance)
admin.site.register(models.Salary)
admin.site.register(models.ApplyLeave)
admin.site.register(models.LeaveType)
admin.site.register(models.LeaveStatus)
admin.site.register(models.Deduction)
admin.site.register(models.Payroll)


# HR Admin Area
hr_site.register(models.Department)
hr_site.register(models.Job)
hr_site.register(models.Employee)
hr_site.register(models.EnrollImage)
hr_site.register(models.Attendance)
hr_site.register(models.Salary)
hr_site.register(models.ApplyLeave)
hr_site.register(models.LeaveType)
hr_site.register(models.LeaveStatus)
hr_site.register(models.Deduction)
hr_site.register(models.Payroll)

