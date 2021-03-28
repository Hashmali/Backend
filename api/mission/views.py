from .serializers import MissionListSerializer,MissionUpdateSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .models import Mission
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import JSONParser


class MissionListView(ListAPIView):
    queryset=Mission.objects.all()
    serializer_class=MissionListSerializer
    #permission_classes=(IsAuthenticated)




class MissionCreateView(CreateAPIView):
    queryset=Mission.objects.all()
    serializer_class=MissionUpdateSerializer
   # permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]

    




class MissionUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Mission.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=MissionUpdateSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]


   