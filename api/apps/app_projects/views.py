from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project
from .serializers import ProjectSerializer
from ..app_users.permissions import IsOwnerOrAdmin, IsOwner


class ProjectListView(generics.ListAPIView):  # get /api/projects/
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [AllowAny]


class ProjectCreateView(generics.CreateAPIView):  # post /api/projects/
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProjectDetailView(generics.RetrieveAPIView):  # get /api/projects/<id>/
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ProjectUpdateView(generics.UpdateAPIView):  # put, patch /api/projects/<id>/
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]


class ProjectDeleteView(generics.DestroyAPIView):  # delete /api/projects/<id>/delete/
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrAdmin]
