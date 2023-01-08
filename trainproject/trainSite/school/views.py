from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from school.models import *
from school.serializers import *


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StatementView(ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class OfficesView(ModelViewSet):
    queryset = Offices.objects.all()
    serializer_class = OfficesSerializer
