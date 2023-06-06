from django.db import models

# Create your models here.
# create user apis


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    # employee_id = models.CharField(max_length=5)
    employeeName = models.CharField(max_length=50)
    employeeAge = models.CharField(max_length=10)
    employeeEmail = models.CharField(max_length=50)
    employeePhoneNo = models.CharField(max_length=10)
    employeeType = models.CharField(max_length=50, choices=(
        ('Manager', 'manager'), ('Senior_Engineer', 'SE'), ('Junior Engineer', 'JE')))
    employeeAddedDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
