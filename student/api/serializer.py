
from student.models import student_custom,application_model
from rest_framework import serializers


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student_custom
        fields = '__all__'

class applicationserializer(serializers.ModelSerializer):
    class Meta:
        model = application_model
        fields = '__all__'