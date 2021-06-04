from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import ExpenseSerializers,IncomeListSerializer,IncomeManageSerializer
from .models import Income,Expense
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser,JSONParser
# Create your views here.
class UpdateExpenseView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Expense.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=ExpenseSerializers
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]


class ListExpensesView(ListAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializers
    permission_classes=(IsAuthenticated,IsAdminUser)


class CreateExpenseView(CreateAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializers
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]

class UpdateIncomeView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Income.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=IncomeManageSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]


class ListIncomesView(ListAPIView):
    queryset=Income.objects.all()
    serializer_class=IncomeListSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)


class CreateIncomeView(CreateAPIView):
    queryset=Income.objects.all()
    serializer_class=IncomeManageSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]
