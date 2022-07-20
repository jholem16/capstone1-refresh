from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.department_name


class Job(models.Model):
    job_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.job_name


class Employee(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now=False)
    gender = models.CharField(
                            max_length=10,
                            choices=(('Male', 'Male'), ('Female', 'Female'),)
                            )
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=50)
    sss_number = models.CharField(max_length=100)
    pagibig_number = models.CharField(max_length=100)
    philhealth_number = models.CharField(max_length=100)
    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return "%s, %s" % (self.lastname, self.firstname)


class EnrollImage(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    image_model = models.ImageField(upload_to='img')
    enroll_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Enrolled Images'

    def __str__(self):
        return "Enrolled Image"


class Attendance(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    attended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.date, self.time)


class Salary(models.Model):
    monthly_rate = models.IntegerField()
    daily_rate = models.IntegerField()
    hourly_rate = models.IntegerField()
    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Salaries'

    def __str__(self):
        return "Salary Rate"


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Leave Types"


class ApplyLeave(models.Model):
    date_from = models.DateField(auto_now=False, blank=True)
    date_to = models.DateField(auto_now=False, blank=True)
    reason = models.CharField(max_length=250, blank=True)
    leave_type = models.ForeignKey(
        LeaveType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Apply Leave"


class LeaveStatus(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    apply_leave = models.ForeignKey(
        ApplyLeave,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Leave Statuses'

    def __str__(self):
        return "Leave Status"


class Deduction(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        null=True,
        blank=True,)
    sss = models.IntegerField()
    pagibig = models.IntegerField()
    philhealth = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Deductions"


class Payroll(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    attendance_id = models.ForeignKey(
        Attendance,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    salary_id = models.ForeignKey(
        Salary,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    deduction_id = models.ForeignKey(
        Deduction,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    leave_status = models.ForeignKey(
        LeaveStatus,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Payroll"
