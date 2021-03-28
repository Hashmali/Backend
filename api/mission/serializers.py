from rest_framework import serializers
from .models import Mission
from api.worker.serializers import UserSerializer
from api.project.serializers import ProjectSerializer



class MissionListSerializer(serializers.ModelSerializer):
    worker=UserSerializer(read_only=True)
    project=ProjectSerializer(read_only=True)
    class Meta:
        model=Mission
        fields="__all__"
        depth = 1



class MissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mission
        fields="__all__"