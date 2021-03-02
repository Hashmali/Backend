from django.urls import path
from rest_framework.authtoken import views

from .views import ScheduleListView,ScheduleUpdateDeleteView,ScheduleCreateView


urlpatterns = [
  path('',ScheduleListView.as_view(),name='list'),
  path('<int:pk>/update/',ScheduleUpdateDeleteView.as_view(),name='manage'),
  path('create/',ScheduleCreateView.as_view(),name='create'),
]
