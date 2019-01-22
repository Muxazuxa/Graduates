from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Student, Cafedra, Faculty
from .forms import StudentForm


class StudentCreateView(CreateView):
    template_name = 'student/create.html'
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return "list"


class StudentListView(ListView):
    context_object_name = 'students'
    template_name = 'student/list.html'

    def get_queryset(self):
        return Student.objects.all()


def load_cafedra(request):
    faculty_id = request.GET.get('faculty')
    cafedra = Cafedra.objects.filter(faculty_id=faculty_id).order_by('name')
    return render(request, 'student/cafedra_dropdown_list_options.html', {'cafedra': cafedra})


