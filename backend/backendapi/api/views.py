from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User
from .serializer import UserSerializer, BookSerializer, ContactUsFormSerializer
from .models import Book, ContactUsFormEnquiry

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	authentication_classes = [TokenAuthentication, ]
	permission_classes = [IsAuthenticated, ]	


class ContactUsFormViewSet(viewsets.ModelViewSet):
	print("contactus")
	queryset = ContactUsFormEnquiry.objects.all()
	serializer_class = ContactUsFormSerializer
	def get(self, request, format=None):
		print("get")
	def post(self, request):
		print("post")
		print(request)