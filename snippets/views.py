from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions # To create permissions for certain views (Not totally necassary, but I want to specify)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.permissions import AllowAny # for using a decorator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied

from .serializers import UserSerializer

from .models import Group
from .serializers import GroupSerializer
from .models import Snippet
from .serializers import SnippetSerializer
from .models import File
from .serializers import FileSerializer

# Automatically generate a token
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Code Group Create View
@permission_classes((AllowAny, )) # Allow all users to use this view without being authenticated
class UserCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	serializer_class = UserSerializer # Serializer has to be inside the initial generic method
	'''
	def get_queryset(self): # This is a default method so use this. Don't define custom function or it won't pass context "self" argument
		user = self.request.user
		queryset = User.objects.filter(owner=user) # Only get groups by the current logged in user
		return queryset # Return data!

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save(owner=self.request.user) # Save owner field in model to the request user
		'''

# Create a view for querying 1 user
class UserView(APIView):
	# Get request
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user_object = self.get_object(pk)
		serializer = UserSerializer(user_object)
		return Response(serializer.data)

	def patch(self, request, pk):
		user_model = self.get_object(pk)
		serializer = UserSerializer(user_model, data=request.data, partial=True) # Partial allows for editing only part of the data
		# Check if serializer is valid and clean data, else return errors
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user_object = self.get_object(pk)
		if user_object != request.user:
			# Don't let user delete if current request.user object isn't user - return FORBIDDEN 403 error
			raise PermissionDenied({"error": "You don't have permission to delete this user"})
		else:
			user_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Code Group Create View
class GroupCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	serializer_class = GroupSerializer # Serializer has to be inside the initial generic method

	def get_queryset(self): # This is a default method so use this. Don't define custom function or it won't pass context "self" argument
		user = self.request.user
		queryset = Group.objects.filter(owner=user) # Only get groups by the current logged in user
		return queryset # Return data!

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save(owner=self.request.user) # Save owner field in model to the request user

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

	def patch(self, request, pk):
		group_model = self.get_object(pk)
		serializer = GroupSerializer(group_model, data=request.data, partial=True) # Partial allows for editing only part of the data
		# Check if serializer is valid and clean data, else return errors
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		group_object = self.get_object(pk)
		group_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Snippet Create View
class SnippetCreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api, and utilizes the Django Web Browseable API"""
	serializer_class = SnippetSerializer

	def get_queryset(self): # This is a default method so use this. Don't define custom function or it won't pass context "self" argument
		user = self.request.user
		queryset = Snippet.objects.filter(owner=user) # Only get groups by the current logged in user
		return queryset # Return data!

	def perform_create(self, serializer):
		"""Save the post data when creating a new snippet"""
		serializer.save(owner=self.request.user) # Save owner field in model to the request user

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

	def patch(self, request, pk):
		snippet_model = self.get_object(pk)
		serializer = SnippetSerializer(snippet_model, data=request.data, partial=True) # Partial allows for editing only part of the data
		# Check if serializer is valid and clean data, else return errors
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		snippet_object = self.get_object(pk)
		snippet_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

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

	def patch(self, request, pk):
		file_model = self.get_object(pk)
		serializer = FileSerializer(file_model, data=request.data, partial=True) # Partial allows for editing only part of the data
		# Check if serializer is valid and clean data, else return errors
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		file_object = self.get_object(pk)
		file_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)