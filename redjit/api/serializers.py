from rest_framework import serializers
from core.models import Link, Comment

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Link

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment
