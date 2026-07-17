from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title","created_at",'image','content',"updated_at"]
        read_only_fields = ["created_at",'id','updated_at']