from django.urls import path
from rest_framework.authtoken import views

from .views import ReportListView,ReportUpdateDeleteView,ReportCreateView


urlpatterns = [
  path('',ReportListView.as_view(),name='list'),
  path('<int:pk>/update/',ReportUpdateDeleteView.as_view(),name='manage'),
  path('create/',ReportCreateView.as_view(),name='create'),
]
