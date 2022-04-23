from rest_framework import serializers
from .models import Student, Teacher


class StudentListSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'teachers']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'subject']


class StudentDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'teachers']
        depth = 1


