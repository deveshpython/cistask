from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task, CustomUser
from .serializers import TaskSerializer, UserSerializer, RegisterSerializer
from .permissions import IsAdmin, IsManager, IsUser, IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.utils.timezone import now, timedelta


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @action(detail=True, methods=['post'], permission_classes=[IsAdmin|IsManager])
    def activate(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'status': 'user activated'})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if self.request.user.role in ['admin', 'manager']:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=self.request.user)