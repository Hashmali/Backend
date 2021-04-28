from rest_framework import serializers
from .models import Report
from api.worker.serializers import UserSerializer
from api.project.serializers import ProjectSerializer




class ReportListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=(
            '__all__'
        )





class ReportUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=(
            '__all__'
        )