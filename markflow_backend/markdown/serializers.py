from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source='tags'
    )

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'updated_at', 'tags', 'tag_ids']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
