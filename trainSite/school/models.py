from django.db import models


# Create your models here.
class Teacher(models.Model):
    fio = models.CharField(null=False, max_length=150)
    experience = models.IntegerField(null=False)
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT)
    student = models.ManyToManyField(
        to="Student", related_name="student", through="Statement")

    def __str__(self):
        return self.fio


class Student(models.Model):
    fio = models.CharField(null=False, max_length=150)
    grade = models.IntegerField(null=False)
    teacher = models.ManyToManyField(
        to="Teacher", related_name="teacher", through="Statement")

    def __str__(self):
        return self.fio


class Statement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    quarter = models.IntegerField(null=False)


class Subject(models.Model):
    title = models.CharField(null=False, max_length=150)
    numberOfHours = models.IntegerField(null=False)

    def __str__(self):
        return self.title


class Offices(models.Model):
    title = models.CharField(null=False, max_length=150)
    number = models.IntegerField(null=False)
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
