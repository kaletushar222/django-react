from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, ContactUsFormEnquiry
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= User
		fields 	= ['id', 'username', 'password']
		extra_kwargs = { 'password' :{ 'write_only' :True, 'required': True }}

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Book
		fields 	= ['id', 'title']

class ContactUsFormSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= ContactUsFormEnquiry
		fields 	= ['name', 'email', 'subject', 'message']