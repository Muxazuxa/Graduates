from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentCreateView.as_view(), name='student_add'),
    path('ajax/load-cafedra/', views.load_cafedra, name='ajax_load_cafedra'),
    path('success', views.success, name='success'),
]
