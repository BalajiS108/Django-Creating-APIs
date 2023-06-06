
from rest_framework import serializers
from api.models import Employee
# create serialisers here


class EmployeeSerialisers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
