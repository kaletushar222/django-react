from django.db import models

class Book(models.Model):
	title = models.TextField(max_length=32, blank=False, null=False)

class ContactUsFormEnquiry(models.Model):
	name = models.TextField(max_length=30, blank=False, null=False)
	email = models.TextField(max_length=100, blank=False, null=False)
	subject = models.TextField(max_length=200, blank=False, null=False)
	message = models.TextField(max_length=500, blank=False, null=False)