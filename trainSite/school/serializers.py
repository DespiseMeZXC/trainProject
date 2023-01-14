from rest_framework import serializers

from school.models import *




class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    # subject = SubjectSerializer()
    class Meta:
        model = Teacher
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
