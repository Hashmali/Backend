from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import ScheduleUpdateSerializers,ScheduleListSerializers
from .models import Schedule
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser,JSONParser




class ScheduleListView(ListAPIView):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleListSerializers
   # permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]



class ScheduleCreateView(CreateAPIView):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleUpdateSerializers
   # permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]

    




class ScheduleUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Schedule.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=ScheduleUpdateSerializers
    permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]


