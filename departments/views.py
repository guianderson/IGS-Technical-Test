from django.shortcuts import render
from departments.serializers import DepartmentSerializer
from .models import Department
from rest_framework import viewsets

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {"departments": departments})

def add_department(request):
    department_name = request.POST.get('department_name')
    Department.objects.create(name=department_name)
    return department_list(request)

def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    return department_list(request)