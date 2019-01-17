from django.contrib import admin
from .models import Cafedra, Faculty, Student

# Register your models here.

admin.site.register(Cafedra)
admin.site.register(Faculty)
admin.site.register(Student)