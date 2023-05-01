from django.urls import path
from .views import department_list, add_department, delete_department

urlpatterns = [
    path('', department_list),
    path('add/', add_department, name='add_department'),
    path('remove/<int:department_id>/', delete_department, name='delete_department')
]