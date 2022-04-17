from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age']
