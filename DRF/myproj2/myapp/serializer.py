from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = ('__all__')


    def validate(self,data):
            
        print(data['age'])

        if data['age'] < 18:
            raise serializers.DjangoValidationError("Age should be grater than 18")
            
        return data