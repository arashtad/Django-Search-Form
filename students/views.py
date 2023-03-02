from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import Student


class Home(TemplateView):
    template_name = "home.html"

class Search(ListView):
    model = Student
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Student.objects.filter(
            Q(firstname__icontains = query) | Q(firstname__icontains = query)
        )