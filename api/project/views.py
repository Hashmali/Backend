from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,ListCreateAPIView
from .serializers import ProjectSerializer,FileSerializers
from .models import Project,File
from rest_framework.parsers import MultiPartParser,JSONParser

# Create your views here.
class ProjectView(ListAPIView):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
   # permission_classes=(IsAuthenticated,)
    parser_classes = [MultiPartParser,JSONParser]

   

class FileView(RetrieveUpdateDestroyAPIView):
    serializer_class=FileSerializers
    queryset=File.objects.all()
    parser_classes = [MultiPartParser,JSONParser]

class CreateFileView(CreateAPIView):
    serializer_class=FileSerializers
    queryset=File.objects.all()
    parser_classes = [MultiPartParser,JSONParser]

class CreateProjectView(CreateAPIView):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
   # permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]

class ManageProjectView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectSerializer
    def get_queryset(self):
        queryset = Project.objects.filter(id=self.kwargs["pk"])
        return queryset
    permission_classes=(IsAuthenticated,IsAdminUser)
    parser_classes = [MultiPartParser,JSONParser]
