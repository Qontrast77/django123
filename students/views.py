from django.views.generic import TemplateView
from students.models import Student
from typing import Any

class ShowStudentsView(TemplateView):
    template_name = "students/show_students.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        
        return context