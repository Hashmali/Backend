from django.urls import path
from rest_framework.authtoken import views

from .views import MissionListView,MissionUpdateDeleteView,MissionCreateView


urlpatterns = [
  path('',MissionListView.as_view(),name='list'),
  path('<int:pk>/update/',MissionUpdateDeleteView.as_view(),name='manage'),
  path('create/',MissionCreateView.as_view(),name='create'),
]
