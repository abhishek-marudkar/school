from main.models import School, Students
from rest_framework import serializers

# Serializers define the API representation.


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'created_at', 'updated_at']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Students
        fields = ['id', 'name', 'enrollment',
                  'school', 'created_at', 'updated_at']


class StudentsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class SchoolStudentSerializer(serializers.ModelSerializer):
    stud = StudentsDataSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'
