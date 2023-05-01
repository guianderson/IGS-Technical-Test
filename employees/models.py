from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, related_name='employees')
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name