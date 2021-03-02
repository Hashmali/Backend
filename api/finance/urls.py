from django.urls import path
from rest_framework.authtoken import views

from .views import ListExpensesView,ListIncomesView,CreateExpenseView,UpdateExpenseView,CreateIncomeView,UpdateIncomeView


urlpatterns = [
  path('expenses/',ListExpensesView.as_view(),name='exp'),
  path('incomes/',ListIncomesView.as_view(),name='inc'),
  path('<int:pk>/expupdate/',UpdateExpenseView.as_view()),
  path('<int:pk>/incupdate/',UpdateIncomeView.as_view()),
  path('expenses/create/',CreateExpenseView.as_view(),name='exp'),
  path('incomes/create/',CreateIncomeView.as_view(),name='inc'),
]
