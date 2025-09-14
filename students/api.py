from rest_framework.viewsets import GenericViewSet

from students.models import Student

class StudentsViewSet(GenericViewSet):
    queryset = Student.objects.all()
