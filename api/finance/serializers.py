from rest_framework import serializers
from .models import Expense,Income
from api.worker.serializers import UserSerializer
from api.project.serializers import ProjectSerializer


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=(
            '__all__'
            )


class IncomeSerializer(serializers.ModelSerializer):
    project=ProjectSerializer(many=True,read_only=True)
    class Meta:
        model = Income
        fields=(
           '__all__'
            )
    
