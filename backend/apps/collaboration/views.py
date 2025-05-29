# backend/apps/collaboration/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, TeamMember, Document, Comment
from .serializers import TeamSerializer, TeamMemberSerializer, DocumentSerializer, CommentSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['created_by']
    search_fields = ['name', 'description']
    
    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        # Add creator as admin
        TeamMember.objects.create(team=team, user=self.request.user, role='admin')
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        team = self.get_object()
        members = TeamMember.objects.filter(team=team)
        serializer = TeamMemberSerializer(members, many=True)
        return Response(serializer.data)

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['team', 'user', 'role']

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['team', 'created_by']
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['document', 'user']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
