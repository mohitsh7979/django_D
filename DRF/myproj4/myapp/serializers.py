from rest_framework import serializers
from .models import student,Subject


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    subject  = SubjectSerializer()
    class Meta:

        model = student
        fields = ('__all__')
        # depth = 1