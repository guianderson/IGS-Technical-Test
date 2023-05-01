from departments.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Department
        fields = '__all__'