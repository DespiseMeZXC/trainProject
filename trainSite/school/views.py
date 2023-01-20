from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from school.models import *
from school.serializers import *
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о учителях", operation_summary="Вывести информацию о учителях"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Добавить учителя", operation_summary="Добавить учителя"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удалить учителя", operation_summary="Удалить учителя"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновить информацию о учителе", operation_summary="Обновить информацию о учителе"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о учителе", operation_summary="Вывести информацию о учителе"
))
class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TeacherSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о предметах", operation_summary="Вывести информацию о предметах"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Добавить предмет", operation_summary="Добавить предмет"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удалить предмет", operation_summary="Удалить предмет"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновить информацию о предмете", operation_summary="Обновить информацию о предмете"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о предмете", operation_summary="Информация о предмете"
))
class SubjectView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о студентах", operation_summary="Вывести информацию о студентах"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Добавить студента", operation_summary="Добавить студента"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удалить студента", operation_summary="Удалить студента"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновить информацию о студенте", operation_summary="Обновить информацию о студенте"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о студенте", operation_summary="Информация о студенте"
))
class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о успеваемости", operation_summary="Вывести информацию о успеваемости"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Добавить информацию о успеваемости", operation_summary="Добавить информацию о успеваемости"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удалить информацию о успеваемости", operation_summary="Удалить информацию о успеваемости"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновить информацию о успеваемости", operation_summary="Обновить информацию о успеваемости"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о конкретной успеваемости", operation_summary="Информация о конкректной успеваемости"
))
class StatementView(ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = (IsAuthenticated, )


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о классах", operation_summary="Вывести информацию о классах"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Добавить класс", operation_summary="Добавить класс"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удалить класс", operation_summary="Удалить класс"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновить информацию о классе", operation_summary="Обновить информацию о классе"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Вывести информацию о классе", operation_summary="Информация о классе"
))
class OfficesView(ModelViewSet):
    queryset = Offices.objects.all()
    serializer_class = OfficesSerializer
    permission_classes = (IsAuthenticated, )
