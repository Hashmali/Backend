from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.authtoken import views
from .views import CustomObtainAuthToken
from .views import UserView,RegistrationView,LogoutView,UpdateUserView,UserViewView


urlpatterns = [
  path('',UserView.as_view(),name=''),
  path('login/',CustomObtainAuthToken.as_view()),
  path('register/',RegistrationView.as_view()),
  path('logout/',LogoutView.as_view()),
  path('<int:pk>/edit/',UpdateUserView.as_view()),
  path('<int:pk>/view/',UserViewView.as_view()),
]
