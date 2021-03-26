from rest_framework import serializers
from .models import Schedule
#from api.worker.serializers import UserSerializer
from api.project.serializers import ProjectSerializer




class ScheduleListSerializers(serializers.ModelSerializer):
  #  worker=UserSerializer(read_only=True)
    project=ProjectSerializer(read_only=True)
    class Meta:
        model=Schedule
        fields=(
            '__all__'
        )
        depth = 1





class ScheduleUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields=(
            '__all__'
        )