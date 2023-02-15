from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Author, Post, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'displayName', 'email', 'host', 'github', 'profile_image', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # hash password
        validated_data['password'] = make_password(validated_data['password'])
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):       
        instance.displayName = validated_data.get('displayName', instance.displayName)
        instance.email = validated_data.get('email', instance.email)
        instance.host = validated_data.get('host', instance.host)
        instance.github = validated_data.get('github', instance.github)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance

class PostSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField()
    author = AuthorSerializer(read_only=True)
    author_id = serializers.CharField(write_only = True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'source', 'origin', 'description', 'content', 'contentType', 'published', 'visibility', 'categories', 'unlisted', 'author', 'type', 'author_id']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):       
        instance.title = validated_data.get('title', instance.title)
        instance.source = validated_data.get('source', instance.source)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.contentType = validated_data.get('contentType', instance.contentType)
        instance.published = validated_data.get('published', instance.published)
        instance.visibility = validated_data.get('visibility', instance.visibility)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.unlisted = validated_data.get('unlisted', instance.unlisted)
        instance.save()
        return instance 

class CommentSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField()
    author = AuthorSerializer(read_only=True)
    author_id = serializers.CharField(write_only = True)
    post_id = serializers.CharField(write_only = True)

    class Meta:
        model = Comment
        fields = ('type', 'id', 'comment', 'contentType', 'published', 'author', 'author_id', 'post_id')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.contentType = validated_data.get('contentType', instance.contentType)
        instance.save()
        return instance
