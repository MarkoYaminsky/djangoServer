from .models import Student, Teacher
from .serializers import StudentListSerializer, StudentDetailSerializer, TeacherSerializer
from rest_framework import viewsets
from rest_framework.views import Response, status
from django.shortcuts import redirect


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):  # create & update M2M
    lookup_field = 'id'
    queryset = Student.objects.all()
    serializer_classes = {'list': StudentListSerializer,
                          'retrieve': StudentDetailSerializer}
    default_serializer_class = StudentDetailSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = self.queryset

        first_name = self.request.query_params.get('first_name')
        if first_name is not None:
            queryset = queryset.filter(first_name__iexact=first_name)

        last_name = self.request.query_params.get('last_name')
        if last_name is not None:
            queryset = queryset.filter(last_name__iexact=last_name)

        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        new_student = Student.objects.create(first_name=data['first_name'],
                                             last_name=data['last_name'],
                                             age=data['age'])
        new_student.save()
        for teacher in data['teachers']:
            teacher_obj = Teacher.objects.get(id__exact=teacher['id'])
            new_student.teachers.add(teacher_obj)
        serializer = StudentListSerializer(new_student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data
        new_student = Student.objects.get(pk=data['id'])
        serializer = StudentDetailSerializer(new_student, data=data)
        new_student.first_name = data['first_name']
        new_student.last_name = data['last_name']
        new_student.age = data['age']
        new_student.save()
        new_student.teachers.clear()
        for teacher in data['teachers']:
            teacher_obj = Teacher.objects.get(id__exact=teacher['id'])
            new_student.teachers.add(teacher_obj)
        if serializer.is_valid():
            new_student.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = self.queryset

        subject = self.request.query_params.get('subject')
        if subject is not None:
            queryset = queryset.filter(subject__iexact=subject)

        return queryset
