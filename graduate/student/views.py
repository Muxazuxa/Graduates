from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Student, Cafedra, Faculty
from .forms import StudentForm


class StudentCreateView(CreateView):
    template_name = 'student/create.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student:success')


def load_cafedra(request):
    faculty_id = request.GET.get('faculty')
    cafedra = Cafedra.objects.filter(faculty_id=faculty_id).order_by('name')
    return render(request, 'student/cafedra_dropdown_list_options.html', {'cafedra': cafedra})


def success(request):
    return render(request, 'student/success.html')

