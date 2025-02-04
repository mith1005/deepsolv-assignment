from rest_framework import serializers
from .models import FacebookPage, Post

class FacebookPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPage
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
