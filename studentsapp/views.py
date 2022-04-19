from .models import Student
from .serializers import StudentSerializer
from rest_framework import mixins, viewsets
from rest_framework.views import Response, status


# Create your views here.
class StudentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = self.queryset

        first_name = self.request.query_params.get('first_name')
        if first_name is not None:
            queryset = queryset.filter(first_name__iexact=first_name)

        last_name = self.request.query_params.get('last_name')
        if last_name is not None:
            queryset = queryset.filter(last_name__iexact=last_name)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
