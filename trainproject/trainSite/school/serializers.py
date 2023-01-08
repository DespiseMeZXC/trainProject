from rest_framework import serializers

from school.models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = "__all__"


class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = "__all__"
