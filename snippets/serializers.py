from rest_framework import serializers

from .models import Snippet, File

# Serializer to create representations of data into JSON. Using ModelSerializer for ease of use
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        files = serializers.StringRelatedField(many=True) # StringRelated outputs the whole string, instead of just the ID
        fields = ('id', 'title', 'description', 'files')
        read_only_fields = ('created', 'modified')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'snippet_id', 'title', 'description', 'language', 'code')