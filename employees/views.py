from django.shortcuts import render
from django.shortcuts import get_object_or_404

from employees.models import Employees
from departments.models import Department

from employees.serializers import EmployeesSerializer
from rest_framework import viewsets


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

def employees_list(request):
    employees = Employees.objects.all()
    return render(request, 'employees_list.html', {"employees": employees})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'employees_list.html', {"departments": departments})

def add_employee(request):
    employee_name = request.POST.get('employee_name')
    employee_department_id = request.POST.get('employee_department')
    employee_department = get_object_or_404(Department, id=employee_department_id)
    employee_email = request.POST.get('employee_email')
    Employees.objects.create(name=employee_name, department=employee_department, email=employee_email)
    return employees_list(request)

def delete_employee(request, employee_id):
    employee = Employees.objects.get(id=employee_id)
    employee.delete()
    return employees_list(request)

