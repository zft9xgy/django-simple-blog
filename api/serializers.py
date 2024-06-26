from rest_framework import serializers
from blog.models import Post,Tag
from django.contrib.auth.models import User



class TagSerializer(serializers.ModelSerializer):

    post_count = serializers.SerializerMethodField()
    total_post = serializers.SerializerMethodField()
    total_tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = '__all__' 

    def get_post_count(self, obj):
        return obj.posts.count()

    def get_total_tags(self,obj):
        tags = Tag.objects.all().count()
        return tags

    def get_total_post(self,obj):
        posts = Post.objects.all().count()
        return posts


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__' 
