from django.contrib import admin
from django.urls import path, include
from departments.views import DepartmentViewSet
from rest_framework import routers

from employees.views import EmployeesViewSet


department_router = routers.DefaultRouter()
department_router.register(r'departments', DepartmentViewSet)

employees_router = routers.DefaultRouter()
employees_router.register(r'employees', EmployeesViewSet)

urlpatterns = [
    path('api/', include(department_router.urls)),
    path('api/', include(employees_router.urls)),
    path('admin/', admin.site.urls),
    path('department/', include('departments.urls')),
    path('', include('employees.urls')),
]
