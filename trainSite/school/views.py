from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, action
from school.models import *
from school.serializers import *
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = TeacherSerializer

    @swagger_auto_schema(method='post', operation_description="Добавить учителя", operation_summary="Добавить учителя")
    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(method='get', operation_description="Вывести учителей учителей", operation_summary="Вывести учителей учителей")
    @action(detail=True, methods=['get'])
    def list(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(method='delete', operation_description="Удалить учителя", operation_summary="Удалить учителя")
    @action(detail=True, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(method='put', operation_description="Обновить информацию о учителе", operation_summary="Обновить информацию о учителе")
    @action(detail=True, methods=['put'])
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(method='get', operation_description="Информация о учителе", operation_summary="Информация о учителе")
    @action(detail=True, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        pass


class SubjectView(ModelViewSet):
    """Работа с предметами"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )


class StatementView(ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = (IsAuthenticated, )


class OfficesView(ModelViewSet):
    queryset = Offices.objects.all()
    serializer_class = OfficesSerializer
    permission_classes = (IsAuthenticated, )
