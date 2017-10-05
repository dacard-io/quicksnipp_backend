from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Group, Snippet, File

# Serializer to create representations of data into JSON. Using ModelSerializer for ease of use
class UserSerializer(serializers.ModelSerializer):
    #groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'snippet_id', 'title', 'description', 'language', 'code')

class SnippetSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        files = serializers.StringRelatedField(many=True) # StringRelated outputs the whole string, instead of just the ID
        fields = ('id', 'group_id', 'title', 'description', 'files')
        read_only_fields = ('created', 'modified')

class GroupSerializer(serializers.ModelSerializer):
    snippets = SnippetSerializer(many=True, read_only=True)  # StringRelated outputs the whole string, instead of just the ID

    class Meta:
        model = (Group)
        fields = ('id', 'title', 'label_color', 'snippets')