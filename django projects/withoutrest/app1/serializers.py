from rest_framework import serializers
# from rest_framework import Employee
from.models import Employee
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
    fields='__all__'