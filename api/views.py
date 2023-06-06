from django.shortcuts import render
from rest_framework import viewsets
from api.models import Employee
from api.serialisers import EmployeeSerialisers

# Create your views here.


class employeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialisers
