from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import permissions # To create permissions for certain views (Not totally necassary, but I want to specify)

from .models import Group
from .serializers import GroupSerializer
from .models import Snippet
from .serializers import SnippetSerializer
from .models import File
from .serializers import FileSerializer

# Code Group Create View
class GroupCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save()

# Create a view for querying 1 code group
class GroupView(APIView):
	# Get request
	def get_object(self, pk):
		try:
			return Group.objects.get(pk=pk)
		except Group.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		group_object = self.get_object(pk)
		serializer = GroupSerializer(group_object)
		return Response(serializer.data)

# Snippet Create View
class SnippetCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save()

# Create a view for querying 1 snippet
class SnippetView(APIView):
	# Get request
	def get_object(self, pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet_object = self.get_object(pk)
		serializer = SnippetSerializer(snippet_object)
		return Response(serializer.data)

class FileCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	queryset = File.objects.all()
	serializer_class = FileSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save()

# Create a view for querying 1 file
class FileView(APIView):
	# Get request
	def get_object(self, pk):
		try:
			return File.objects.get(pk=pk)
		except File.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		file_object = self.get_object(pk)
		serializer = FileSerializer(file_object)
		return Response(serializer.data)