from rest_framework import serializers
from .models import Report
from api.worker.serializers import UserSerializer
from api.project.serializers import ProjectSerializer




class ReportListSerializers(serializers.ModelSerializer):
    worker=UserSerializer(read_only=True)
    project=ProjectSerializer(read_only=True)
    class Meta:
        model=Report
        fields=(
            '__all__'
        )
        depth = 1





class ReportUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=(
            '__all__'
        )