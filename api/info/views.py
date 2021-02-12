from .serializers import InfoSerializers,CarSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from .models import Info,Car
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import JSONParser

class InfoUpdateView(RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = Info.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=InfoSerializers
    permission_classes=[IsAuthenticated,IsAdminUser]
    parser_classes = [MultiPartParser,JSONParser]

class InfoListView(RetrieveAPIView):
    def get_queryset(self):
        queryset = Info.objects.filter(id=self.kwargs["pk"])
        return queryset    
    serializer_class=InfoSerializers
    permission_classes=[IsAuthenticated,]
class CarView(RetrieveUpdateDestroyAPIView):
    serializer_class=CarSerializer
    def get_queryset(self):
        queryset = Car.objects.filter(id=self.kwargs["pk"])
        return queryset
    permission_classes=[IsAuthenticated,]