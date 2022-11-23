from drfCRUD_app import models
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer