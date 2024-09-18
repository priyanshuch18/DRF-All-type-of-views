from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        # field = "__all__"
        fields = ['title','email','author']