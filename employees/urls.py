from django.urls import path
from .views import employees_list, add_employee, delete_employee, department_list

urlpatterns = [
    path('', employees_list),
    path('employee-form/', department_list, name='department_list'),
    path('add/', add_employee, name='add_employee'),
    path('delete/<int:employee_id>/', delete_employee, name='delete_employee'),
]
