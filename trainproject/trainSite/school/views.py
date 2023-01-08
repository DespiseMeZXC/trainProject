from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from school.models import *
from school.serializers import *


class TeacherAPI:
    class TeacherAPIListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
        queryset = Teacher.objects.all()
        serializer_class = TeacherSerializer

    class TeacherAPIUpdateDestroyRetrieve(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                                          GenericViewSet):
        queryset = Teacher.objects.all()
        serializer_class = TeacherSerializer


class SubjectAPI:
    class SubjectAPIListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer

    class SubjectAPIUpdateDestroyRetrieve(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                                          GenericViewSet):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer


class StudentAPI:
    class StudentAPIListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

    class StudentAPIUpdateDestroyRetrieve(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                          mixins.RetrieveModelMixin,
                                          GenericViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer


class StatementAPI:
    class StatementAPIListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
        queryset = Statement.objects.all()
        serializer_class = StatementSerializer

    class StatementAPIUpdateDestroyRetrieve(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                            mixins.RetrieveModelMixin,
                                            GenericViewSet):
        queryset = Statement.objects.all()
        serializer_class = StatementSerializer


class OfficesAPI:
    class OfficesAPIListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
        queryset = Offices.objects.all()
        serializer_class = OfficesSerializer

    class OfficesAPIUpdateDestroyRetrieve(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                          mixins.RetrieveModelMixin,
                                          GenericViewSet):
        queryset = Offices.objects.all()
        serializer_class = OfficesSerializer
