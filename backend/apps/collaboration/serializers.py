# backend/apps/collaboration/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, TeamMember, Document, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    
    class Meta:
        model = TeamMember
        fields = ['id', 'team', 'user', 'user_id', 'role', 'joined_at']

class TeamSerializer(serializers.ModelSerializer):
    members_count = serializers.SerializerMethodField()
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members_count', 'created_by', 'created_by_name', 'created_at', 'updated_at']
    
    def get_members_count(self, obj):
        return obj.members.count()

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'document', 'user', 'user_name', 'text', 'created_at', 'updated_at']

class DocumentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'team', 'created_by', 'created_by_name', 'comments', 'created_at', 'updated_at']
