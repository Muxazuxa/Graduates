from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentCreateView.as_view(), name='student_add'),
    path('list', views.StudentListView.as_view(), name='student_list'),
    path('ajax/load-cafedra/', views.load_cafedra, name='ajax_load_cafedra'),
]
