from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import ReportUpdateSerializers,ReportListSerializers
from .models import Report
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser,JSONParser




class ReportListView(ListAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportListSerializers
   # permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]



class ReportCreateView(CreateAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportUpdateSerializers
   # permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]

    




class ReportUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Report.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class=ReportUpdateSerializers
    permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]


