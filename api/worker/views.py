from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .serializers import UserSerializer,RegistrationSerializer,LogoutSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser,JSONParser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

User = get_user_model()

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})



class UserView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class RegistrationView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=RegistrationSerializer
    queryset=User.objects.all()
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)




class LogoutView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=LogoutSerializer
    queryset= User.objects.all()
    def get(self,request,*args,**kwargs):
        request.user.auth_token.delete()
        content = 'success'
        return Response(content,status=status.HTTP_200_OK)



class UpdateUserView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = RegistrationSerializer
   # permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]





class UserViewView(RetrieveAPIView):
    
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]
    
    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs["pk"])
        return queryset