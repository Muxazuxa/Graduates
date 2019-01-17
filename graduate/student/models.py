from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Cafedra(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    fio = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False)
    enter_date = models.DateField(blank=False)
    graduate_date = models.DateField(blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    cafedra = models.ForeignKey(Cafedra,on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    job = models.CharField(max_length=100, blank=False)
    dolj = models.CharField(max_length=50, blank=False)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.fio

