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
    permission_classes = (IsAuthenticated,)
    serializer_class = TeacherSerializer

    @swagger_auto_schema(method='post', operation_description="Добавить учителя", operation_summary="Добавить учителя")
    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(method='get', operation_description="Вывести учителей учителей", operation_summary="Вывести учителей учителей")
    @action(detail=True, methods=['get'])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(method='delete', operation_description="Удалить учителя", operation_summary="Удалить учителя")
    @action(detail=True, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(method='put', operation_description="Обновить информацию о учителе", operation_summary="Обновить информацию о учителе")
    @action(detail=True, methods=['put'])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @swagger_auto_schema(method='get', operation_description="Информация о учителе", operation_summary="Информация о учителе")
    @action(detail=True, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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
