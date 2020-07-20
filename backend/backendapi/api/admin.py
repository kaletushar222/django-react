from django.contrib import admin
from .models import Book, ContactUsFormEnquiry

# Register your models here.

admin.site.register(Book)
admin.site.register(ContactUsFormEnquiry)