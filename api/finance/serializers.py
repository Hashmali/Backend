from rest_framework import serializers
from .models import Expense,Income
from api.project.serializers import ProjectSerializer


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=(
            '__all__'
            )


class IncomeListSerializer(serializers.ModelSerializer):
    project=ProjectSerializer(read_only=True)
    class Meta:
        model = Income
        fields=(
           '__all__'
            )
       


class IncomeManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields=(
           '__all__'
            )    
